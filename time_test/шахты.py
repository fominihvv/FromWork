import asyncio
from dataclasses import dataclass, field


@dataclass
class Storage:
    quantity: int


@dataclass
class Jobs:
    jobs: list = field(default_factory=list)


class Gather:

    def __init__(self, all_storage, storage, resource_mining: asyncio.Condition, stop_work: asyncio.Event, efficiency: int, name: str):
        self.resource_mining = resource_mining
        self.stop_work = stop_work
        self.all_storage = all_storage
        self.storage = storage
        self.efficiency = efficiency
        self.name = name

    async def gather_resources(self):
        while not self.stop_work.is_set():
            await asyncio.sleep(1)
            if not self.stop_work.is_set():
                async with self.resource_mining:
                    self.storage.quantity += self.efficiency
                    self.all_storage.quantity += self.efficiency
                    if self.all_storage.quantity >= 1_000:
                        self.stop_work.set()
                    print(self)
                    self.resource_mining.notify_all()


class StoneGathering(Gather):
    def __str__(self):
        return f"Шахта {self.name}. Добыто {self.efficiency} ед. камня. На складе {self.storage.quantity} ед. Всего {self.all_storage.quantity} ед."


class MetalGathering(Gather):
    def __str__(self):
        return f"Литейная мастерская {self.name}. Добыто {self.efficiency} ед. металла. На складе {self.storage.quantity} ед. Всего {self.all_storage.quantity} ед."


class ClothGathering(Gather):
    def __str__(self):
        return f"Ткацкая фабрика {self.name}. Добыто {self.efficiency} ед. ткани. На складе {self.storage.quantity} ед. Всего {self.all_storage.quantity} ед."


class CraftItem:
    def __init__(self, storage, required_amount_of_wood: asyncio.Condition, stop_work: asyncio.Event, jobs: Jobs, name: str):
        self.required_amount_of_wood = required_amount_of_wood
        self.stop_work = stop_work
        self.storage = storage
        self.jobs = jobs
        self.create_item = ''
        self.name = name

    async def craft_item(self):
        while not self.stop_work.is_set():
            need_resources = 0
            async with self.required_amount_of_wood:
                await self.required_amount_of_wood.wait()
                if not self.stop_work.is_set():
                    self.create_item, need_resources = self.jobs.jobs[0]
                    if self.storage.quantity >= need_resources:
                        self.storage.quantity -= need_resources
                        print(self)
                        self.jobs.jobs.pop(0)
                        self.jobs.jobs.append((self.create_item, need_resources))

                        if not self.jobs.jobs:
                            self.stop_work.set()

            if not self.stop_work.is_set():
                await asyncio.sleep(need_resources / 10) # На тесте в степике не пройдёт
                #await asyncio.sleep(0)


class StoneCraftItem(CraftItem):
    def __str__(self):
        return f"{self.name}. Изготовлен {self.create_item} из камня."


class MetalCraftItem(CraftItem):
    def __str__(self):
        return f"{self.name}. Изготовлен {self.create_item} из металла."


class ClothCraftItem(CraftItem):
    def __str__(self):
        return f"{self.name}. Изготовлен {self.create_item} из ткани."


async def main():
    stone_resources_dict = {'Каменная плитка': 10, 'Каменная ваза': 40, 'Каменный столб': 50}
    metal_resources_dict = {'Металлическая цепь': 6, 'Металлическая рамка': 24, 'Металлическая ручка': 54}
    cloth_resources_dict = {'Тканевая занавеска': 8, 'Тканевый чехол': 24, 'Тканевое покрывало': 48, }
    stone_jobs, metal_jobs, cloth_jobs = Jobs(), Jobs(), Jobs()
    stone_jobs.jobs = [(key, value) for key, value in stone_resources_dict.items()]
    metal_jobs.jobs = [(key, value) for key, value in metal_resources_dict.items()]
    cloth_jobs.jobs = [(key, value) for key, value in cloth_resources_dict.items()]
    all_storage, stone_storage, metal_storage, cloth_storage = Storage(0), Storage(0), Storage(0), Storage(0)
    stop_stone, stop_metal, stop_cloth = asyncio.Event(), asyncio.Event(), asyncio.Event()
    required_amount_of_stone, required_amount_of_metal, required_amount_of_cloth = asyncio.Condition(), asyncio.Condition(), asyncio.Condition()

    stone_gather_1 = StoneGathering(all_storage, stone_storage, required_amount_of_stone, stop_stone, 10, 'Каменная шахта 1')
    stone_gather_2 = StoneGathering(all_storage, stone_storage, required_amount_of_stone, stop_stone, 10, 'Каменная шахта 2')
    metal_gather_1 = MetalGathering(all_storage, metal_storage, required_amount_of_metal, stop_metal, 6, 'Литейный цех 1')
    metal_gather_2 = MetalGathering(all_storage, metal_storage, required_amount_of_metal, stop_metal, 6, 'Литейный цех 2')
    cloth_gather_1 = ClothGathering(all_storage, cloth_storage, required_amount_of_cloth, stop_cloth, 8, 'Ткацкая фабрика 1')
    cloth_gather_2 = ClothGathering(all_storage, cloth_storage, required_amount_of_cloth, stop_cloth, 8, 'Ткацкая фабрика 2')

    stone_craft_1 = StoneCraftItem(stone_storage, required_amount_of_stone, stop_stone, stone_jobs, 'Каменная мастерская 1')
    stone_craft_2 = StoneCraftItem(stone_storage, required_amount_of_stone, stop_stone, stone_jobs, 'Каменная мастерская 2')
    metal_craft_1 = MetalCraftItem(metal_storage, required_amount_of_metal, stop_metal, metal_jobs, 'Кузница 1')
    metal_craft_2 = MetalCraftItem(metal_storage, required_amount_of_metal, stop_metal, metal_jobs, 'Кузница 2')
    cloth_craft_1 = ClothCraftItem(cloth_storage, required_amount_of_cloth, stop_cloth, cloth_jobs, 'Ателье 1')
    cloth_craft_2 = ClothCraftItem(cloth_storage, required_amount_of_cloth, stop_cloth, cloth_jobs, 'Ателье 2')


    tasks = [stone_gather_1.gather_resources(), stone_gather_2.gather_resources(),
                         metal_gather_1.gather_resources(), metal_gather_2.gather_resources(),
                         cloth_gather_1.gather_resources(), cloth_gather_2.gather_resources(),
                         stone_craft_1.craft_item(), stone_craft_2.craft_item(),
                         metal_craft_1.craft_item(), metal_craft_2.craft_item(),
                         cloth_craft_1.craft_item(), cloth_craft_2.craft_item()]
    loop = asyncio.get_event_loop()
    while not stop_stone.is_set() or not stop_metal.is_set() or not stop_cloth.is_set():
        if tasks:
            for task in tasks:
                asyncio.create_task(task)
            tasks = []
        await asyncio.sleep(0.1)
    print('Добыто:', all_storage.quantity)


if __name__ == "__main__":
    asyncio.run(main())
