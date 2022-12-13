import numpy as np

class Monkey:
    
    def __init__(self, items, operation, div_test, throw_to):
        self.items, self.operation, self.div_test, self.throw_to = items, operation, div_test, throw_to
        self.inspect_count = 0
        
    def update_worry_divide(self, old, *args):
        return eval(self.operation)//3
        
    def update_worry_modulo(self, old, mod):
        return eval(self.operation)%mod
    
    def throw_receiver(self, worry):
        return self.throw_to[int(worry%self.div_test>0)]
    
    @staticmethod
    def from_description(description):
        items = [int(i) for i in description[0].split(":")[-1].split(",")]
        operation = description[1].split("=")[-1]
        div_test, throw_to_T, throw_to_F = [int(line.split()[-1]) for line in description[2:]]
        return Monkey(items, operation, div_test, (throw_to_T, throw_to_F))
    
class MonkeyGroup:
    
    def __init__(self, monkeys, worry_reduction="divide"):
        self.monkeys, self.worry_reduction = monkeys, worry_reduction
        self.lcm = int(np.lcm.reduce([monkey.div_test for monkey in self.monkeys]))
        self.update_worry = Monkey.update_worry_divide if worry_reduction=="divide" else Monkey.update_worry_modulo
    
    def run_rounds(self, N=20):
        for _ in range(N):
            for monkey in self.monkeys:
                for item in monkey.items:
                    monkey.inspect_count += 1
                    worry = self.update_worry(monkey, item, self.lcm)
                    self.monkeys[monkey.throw_receiver(worry)].items.append(worry)
                monkey.items = []
    
    @staticmethod
    def from_description(description, worry_reduction="divide"):
        inds = [i for i,line in enumerate(description) if line.startswith("Monkey")]
        monkeys = [Monkey.from_description(description[i+1:i+6]) for i in inds]
        return MonkeyGroup(monkeys, worry_reduction)
    
    @property
    def monkey_business(self):
        inspect_counts = [monkey.inspect_count for monkey in self.monkeys]
        return np.prod(np.sort(inspect_counts)[-2:],dtype="int64")

with open("input","r") as fich:
    data = fich.read().splitlines()
    
group = MonkeyGroup.from_description(data)
group.run_rounds()

print(f"Level of monkey business after 20 rounds is {group.monkey_business}")
    
group = MonkeyGroup.from_description(data,worry_reduction="modulo")
group.run_rounds(10_000)

print(f"Level of monkey business after 10,000 rounds is {group.monkey_business}")