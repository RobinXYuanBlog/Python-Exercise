import cocos
from cocos.actions import Waves3D, TiledGrid3DAction, Twirl, Lens3D, Waves, Liquid


class MySprite(cocos.layer.Layer):

    def __init__(self):
        super(MySprite, self).__init__()

        sprite = cocos.sprite.Sprite('icon.jpg')
        sprite.position = 240, 320
        self.add(sprite)

        # layer_action = Twirl( grid=(16, 12), duration=3 )

        layer_action = (Waves(grid=(16, 12), duration=4) + Liquid(grid=(16, 12), duration=5))

        self.do(layer_action)


cocos.director.director.init()

sprite = cocos.sprite.Sprite('icon.jpg')
sprite.position = 240, 320

main_scene = cocos.scene.Scene( MySprite() )

# scene_action_1 = Twirl( grid=(16, 12), duration=3 )
# main_scene.do(scene_action_1)

cocos.director.director.run(main_scene)
