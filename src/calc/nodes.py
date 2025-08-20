from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


class AbstractNode(ABC):
    @abstractmethod
    def execute(self) -> int | None:
        pass


@dataclass
class Node(AbstractNode):
    args: List = field(default_factory=list)

    def execute(self):
        last_res = 0
        for node in self.args:
            last_res = node.execute()
        return last_res


@dataclass
class NumberNode(Node):
    data: float = None

    def execute(self):
        return self.data


@dataclass
class AddNode(Node):
    def execute(self):
        return self.args[0].execute() + self.args[1].execute()


@dataclass
class SubNode(Node):
    def execute(self):
        return self.args[0].execute() - self.args[1].execute()


@dataclass
class MulNode(Node):
    def execute(self):
        return self.args[0].execute() * self.args[1].execute()


@dataclass
class DivNode(Node):
    def execute(self):
        return self.args[0].execute() / self.args[1].execute()


@dataclass
class OutNode(Node):
    def execute(self):
        res = self.args[0].execute()
        print(res)
        return 0
