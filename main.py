from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics.transformation import Matrix
from kivy.uix.label import Label
from kivy.config import Config
from kivy.graphics import PushMatrix, PopMatrix, MatrixInstruction

# 配置窗口默认设置
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

class ScreenAdjuster(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(** kwargs)
        self.orientation = 'vertical'
        
        # 初始化缩放值和旋转角度
        self.scale_x = 1.0
        self.scale_y = 1.0
        self.rotation = 0
        
        # 创建示例图像（实际应用中可以替换为摄像头画面或其他内容）
        self.image = Image(source='example.jpg', allow_stretch=True, keep_ratio=False)
        
        # 添加矩阵变换指令
        with self.image.canvas.before:
            PushMatrix()
            self.transform = MatrixInstruction()
        with self.image.canvas.after:
            PopMatrix()
            
        self.add_widget(self.image)
        
        # 添加旋转控制按钮
        rotate_box = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        rotate_box.add_widget(Button(text='横向', on_press=self.rotate_horizontal))
        rotate_box.add_widget(Button(text='纵向', on_press=self.rotate_vertical))
        self.add_widget(rotate_box)
        
        # 添加横向缩放控制
        scale_x_box = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        scale_x_box.add_widget(Label(text='横向缩放'))
        self.scale_x_slider = Slider(min=0.5, max=2.0, value=1.0)
        self.scale_x_slider.bind(value=self.on_scale_x)
        scale_x_box.add_widget(self.scale_x_slider)
        self.add_widget(scale_x_box)
        
        # 添加纵向缩放控制
        scale_y_box = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        scale_y_box.add_widget(Label(text='纵向缩放'))
        self.scale_y_slider = Slider(min=0.5, max=2.0, value=1.0)
        self.scale_y_slider.bind(value=self.on_scale_y)
        scale_y_box.add_widget(self.scale_y_slider)
        self.add_widget(scale_y_box)
        
        # 应用初始变换
        self.update_transform()
    
    def rotate_horizontal(self, instance):
        # 旋转到横向（90度）
        self.rotation = 90
        self.update_transform()
    
    def rotate_vertical(self, instance):
        # 旋转到纵向（0度）
        self.rotation = 0
        self.update_transform()
    
    def on_scale_x(self, instance, value):
        self.scale_x = value
        self.update_transform()
    
    def on_scale_y(self, instance, value):
        self.scale_y = value
        self.update_transform()
    
    def update_transform(self):
        # 创建变换矩阵
        mat = Matrix()
        # 先旋转
        mat = mat.rotate(self.rotation, 0, 0, 1)
        # 再缩放
        mat = mat.scale(self.scale_x, self.scale_y, 1)
        # 应用变换 - 使用新的API方式
        self.transform.matrix = mat
        # 强制刷新
        self.image.canvas.ask_update()

class ScreenAdjusterApp(App):
    def build(self):
        return ScreenAdjuster()
    
    def on_start(self):
        # 应用启动时设置窗口标题
        self.title = '屏幕画面调整工具'

if __name__ == '__main__':
    ScreenAdjusterApp().run()
    