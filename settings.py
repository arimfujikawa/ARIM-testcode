from enum import Enum

FILE_NAME = 'test.png'

# パラメータ用列挙型ベース
class ParameterBase(Enum):
    def __init__(self, minimum, maximum):
        self.MIN = minimum
        self.MAX = maximum

    # NOTE: Enumはインスタンスが必要ないのでメソッドはクラスメソッドで作成する
    @classmethod
    def get_items(cls):
        # items()メソッドを実行
        return [*cls.__members__.items()]

# FEFFFitのパラメータ
class Para(ParameterBase):
    # X、Yの範囲
    x = (0, 5)
    y = (-1, 2)

