import cocos
from cocos.actions import Move, MoveBy, Place, Reverse, Repeat, JumpBy, Bezier, RotateBy, Accelerate, Waves3D, AccelAmplitude

class MyTest(cocos.layer.Layer):

    def __init__(self):
        super(MyTest, self).__init__()

        sprite = cocos.sprite.Sprite('icon.jpg')

        sprite.position = 240, 320
        sprite.scale = 0.5
        self.add(sprite)

        move = MoveBy( (50, 100), duration=2 )

        sprite.do(Repeat(Reverse(move) + move))


class PlaceTest(cocos.layer.Layer):

    def __init__(self):
        super(PlaceTest, self).__init__()

        sprite = cocos.sprite.Sprite('icon.jpg')

        sprite.position = 320, 240
        sprite.scale = 0.5
        self.add(sprite)

        place = Place( (50, 100) )

        sprite.do(place)


class JumpByTest(cocos.layer.Layer):

    def __init__(self):
        super(JumpByTest, self).__init__()

        sprite = cocos.sprite.Sprite('icon.jpg')

        sprite.position = 240, 320
        sprite.scale = 0.5
        self.add(sprite)

        jump = JumpBy( (50, 100), duration=2 )

        sprite.do(Repeat(Reverse(jump) + jump))


class MultiActions(cocos.layer.Layer):

    def __init__(self):
        super(MultiActions, self).__init__()

        sprite = cocos.sprite.Sprite('icon.jpg')

        sprite.position = 240, 320
        sprite.scale = 0.3
        self.add(sprite)

        # action1 = Accelerate(MoveBy( (100, 100), duration=3 ), rate=3)
        # action2 = RotateBy( 360, 5 ) * 2
        # action3 = JumpBy( (-200, -300), duration=2 )
        #
        # actions = action1 + (action2 | action3)
        #
        # sprite.do(Repeat(action=actions))


cocos.director.director.init()
main_scene = cocos.scene.Scene( MultiActions() )
action = AccelAmplitude(Waves3D(waves=4, amplitude=40, duration=6), rate=1.0)
main_scene.do(action=action)
cocos.director.director.run(main_scene)