#Imports the libraries used for this App
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#A kivy method that interprets the following string in kivy language to display the GUI
Builder.load_string("""
<MenuButton@Button>:
    font_size: 30
    size_hint: 0.65, 0.2
    background_normal: 'Button.jpg'
    background_down: 'Button.jpg'
    border: 30, 30, 30, 30, 
    color: 0, 1, 0, 1

<BackButton@Button>:
    font_size: 20
    size_hint: 0.2, 0.1
    background_normal: 'Button.jpg'
    background_down: 'Button.jpg'
    text: 'Back'
    border: 30, 30, 30, 30, 
    color: 0, 1, 0, 1

<CommonLabel@Label>:
    size_hint: 0.5,0.2
    color: 200, 200, 200, 1
    font_size: 22
    text_size: self.size
                
<MenuFloat@FloatLayout>:
    canvas:
        Rectangle:
            source: 'MenuBackground.jpg'
            size: self.size
            pos: self.pos

<MenuScreen>:
    id: MenuScreen
    MenuFloat:
        Label:
            size_hint: 0.52,0.4
            pos_hint: {'x': 0.24, 'y': 0.5}
            text: 'Your Score: 1038'
            color: 200, 200, 200, 1
            font_size: 35 
        MenuButton:
            pos_hint: {'x': 0.2, 'y': 0.46}
            text: 'Missions'
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'MissionsScreen'        
        MenuButton:
            pos_hint: {'x': 0.2, 'y': 0.23}
            text: 'Leaderboard'
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'LeaderboardScreen'
        MenuButton:
            pos_hint: {'x': 0.2, 'y': 0}
            text: 'My Stats'
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'StatsScreen'
        Button:
            font_size: 10
            size_hint: 0.1, 0.05
            background_normal: 'MenuButton.jpg'
            background_down: 'MenuButton.jpg'
            border: 5, 5, 5, 5,
            color: 0, 1, 0, 1
            pos_hint: {'x': 0.9, 'y': 0}
            text: 'Exit'
            on_release: MenuScreen.exit()

<MissionsScreen>:
    id: MissionsScreen
    FloatLayout:
        canvas:
            Rectangle:
                source: 'Background.png'
                size: self.size
                pos: self.pos
        BackButton:
            pos_hint: {'x': 0, 'y': 0}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'MenuScreen'
        MenuButton:
            pos_hint: {'x': 0.2, 'y': 0.7}
            text: 'Diet'
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'DietGoalsScreen'
        MenuButton:
            pos_hint: {'x': 0.2, 'y': 0.45}
            text: 'Driving'
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'DrivingGoalsScreen'
        MenuButton:
            pos_hint: {'x': 0.2, 'y': 0.2}
            text: 'More Coming Soon!'
    
<DietGoalsScreen>:
    id: DietGoalsScreen
    FloatLayout:
        canvas:
            Rectangle:
                source: 'GeneralBackground.jpg'
                size: self.size
                pos: self.pos
        BackButton:
            pos_hint: {'x': 0, 'y': 0}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'MissionsScreen'
        CommonLabel:
            pos_hint: {'x': 0.04, 'y': 0.7}
            text: 'Your diet has produced 14 pounds of C02, which is 6 pounds under your goal of 20 for this week! Good Job!'
        CommonLabel:
            pos_hint: {'x': 0.04, 'y': 0.5}
            text: 'If you succeed this week, you will have reached your goals for the 5th time in a row!'
    
<DrivingGoalsScreen>:
    id: DrivingGoalsScreen
    FloatLayout:
        canvas:
            Rectangle:
                source: 'GeneralBackground.jpg'
                size: self.size
                pos: self.pos
        BackButton:
            pos_hint: {'x': 0, 'y': 0}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'MissionsScreen'
        CommonLabel:
            pos_hint: {'x': 0.04, 'y': 0.7}
            text: 'You have drove 112 miles this week so far, which is 6 miles under goal of 120! Good Job!'
        CommonLabel:
            pos_hint: {'x': 0.04, 'y': 0.5}
            text: 'If you succeed this week, you will have reached your goals for the 3rd time in a row!'
   
<LeaderboardScreen>:
    id: LeaderboardScreen
    FloatLayout:
        canvas:
            Rectangle:
                source: 'Leaderboard.jpg'
                size: self.size
                pos: self.pos
        BackButton:
            pos_hint: {'x': 0, 'y': 0}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'MenuScreen'
        
<StatsScreen>:
    id: StatsScreen
    FloatLayout:
        canvas:
            Rectangle:
                source: 'StatsBackground.jpg'
                size: self.size
                pos: self.pos
        BackButton:
            pos_hint: {'x': 0, 'y': 0}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'MenuScreen'
        CommonLabel:
            pos_hint: {'x': 0.04, 'y': 0.8}
            text: 'Username: User Mcgee'
        CommonLabel:
            pos_hint: {'x': 0.04, 'y': 0.7}
            text: 'Your Score: 1038'
        CommonLabel:
            pos_hint: {'x': 0.04, 'y': 0.6}
            text: 'Miles Driven This week:'
        CommonLabel:
            pos_hint: {'x': 0.7, 'y': 0.6}
            text: '112'
        CommonLabel:
            pos_hint: {'x': 0.04, 'y': 0.5}
            text: 'Pounds of C02 emitted from diet:'
        CommonLabel:
            pos_hint: {'x': 0.7, 'y': 0.5}
            text: '14'
        CommonLabel:
            pos_hint: {'x': 0.04, 'y': 0.4}
            text: 'Total pounds of C02 emitted this week:'
        CommonLabel:
            pos_hint: {'x': 0.7, 'y': 0.4}
            text: '58.8'
        Button:
            font_size: 20
            size_hint: 0.96, 0.14
            background_normal: 'Button.jpg'
            background_down: 'Button.jpg'
            border: 45, 45, 45, 45, 
            color: 0, 1, 0, 1
            pos_hint: {'x': 0.02, 'y': 0.2}
            text: 'Information on calculations'
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'InformationScreen'
        Button:
            font_size: 20
            size_hint: 0.4, 0.14
            background_normal: 'Button.jpg'
            background_down: 'Button.jpg'
            border: 45, 45, 45, 45, 
            color: 0, 1, 0, 1
            pos_hint: {'x': 0.4, 'y': 0.02}
            text: 'Log New Data'
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'LoggingScreen'

<LoggingScreen>:
    id: LoggingScreen
    FloatLayout:
        canvas:
            Rectangle:
                source: 'GeneralBackground.jpg'
                size: self.size
                pos: self.pos
        BackButton:
            pos_hint: {'x': 0, 'y': 0}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'StatsScreen'
        CommonLabel:
            pos_hint: {'x': 0.04, 'y': 0.8}
            text: 'Miles driven:'
        TextInput:
            size_hint: 0.3, 0.05
            pos_hint: {'x': 0.56, 'y': 0.8} 
            multiline: False
            foreground_color: 0, 0, 0, 1
            background_color: 128, 128, 128, 128, 1
        CommonLabel:
            pos_hint: {'x': 0.04, 'y': 0.58}
            text: 'Carbon footprint of food consumed  is'
        Spinner:
            size_hint: None, None
            size: 162, 22
            background_color: 255, 255, 255, 1
            color: 0, 0, 0, 1
            pos_hint: {'x': 0.56, 'y': 0.58}
            text: 'None'
            values: 'Very Heavy', 'Heavy', 'Medium', 'Small', 'Very Small'
        CommonLabel:
            size_hint: 0.7,0.3
            pos_hint: {'x': 0.04, 'y': 0.3}
            text: 'Note that a very heavy meal has 6+ pounds of CO2. A heavy meal has 4.5-5.9 pounds of CO2. A medium meal has 3-4.4 pounds of C02. A small meal has 1.5-2.9 pounds of CO2. A very small meal has 0-1.4 pounds of CO2.'

<InformationScreen>:
    id: InformationScreen
    FloatLayout:
        canvas:
            Rectangle:
                source: 'Information.jpg'
                size: self.size
                pos: self.pos
        BackButton:
            pos_hint: {'x': 0, 'y': 0}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'StatsScreen'
        BackButton:
            pos_hint: {'x': 0, 'y': 0}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'StatsScreen'
""")

#Creates the following screens as objects to view them later in the parent object called ScreenManager
class MenuScreen(Screen):
    def exit(self):
        App.get_running_app().stop()

class MissionsScreen(Screen):
    pass

class LeaderboardScreen(Screen):
    pass

class StatsScreen(Screen):
    pass

class DietGoalsScreen(Screen):
    pass

class DrivingGoalsScreen(Screen):
    pass

class InformationScreen(Screen):
    pass

class LoggingScreen(Screen):
    pass

#Applies the screens to the ScreenManager to make them children of the ScreenManager
screenManager = ScreenManager()
screenManager.add_widget(MenuScreen(name='MenuScreen'))
screenManager.add_widget(MissionsScreen(name='MissionsScreen'))
screenManager.add_widget(LeaderboardScreen(name='LeaderboardScreen'))
screenManager.add_widget(StatsScreen(name='StatsScreen'))
screenManager.add_widget(DietGoalsScreen(name='DietGoalsScreen'))
screenManager.add_widget(DrivingGoalsScreen(name='DrivingGoalsScreen'))
screenManager.add_widget(LoggingScreen(name='LoggingScreen'))
screenManager.add_widget(InformationScreen(name='InformationScreen'))

#Displays and builds the ScreenManager upon running the program
class TestApp(App):
    def build(self):
        return screenManager

#Runs the script while utilizing other files upon running the script
if __name__ == '__main__':
    TestApp().run()
