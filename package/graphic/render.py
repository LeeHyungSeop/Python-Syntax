# from package.sound.echo import echo_test # relavtive package를 이용하여 module을 import
from ..sound.echo import echo_test # 위와 동일한 코드


def render_test() :
    print("render")
    echo_test()