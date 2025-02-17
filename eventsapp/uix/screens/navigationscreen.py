'''Navigation Screen
'''
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.factory import Factory

Factory.register('TouchRippleBehavior', module='uix.behaviors')


class NavigationScreen(Screen):
    '''
    '''

    Builder.load_string('''
#:import load_screen utils.load_screen
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
#:import NavigationDrawer uix.navigationdrawer.NavigationDrawer


<MenuButton@PyConButton>
    group: 'LeftPanel'
    text_size: self.size
    halign: 'left'
    valign: 'center'
    padding: dp(15), dp(15)
    color: app.base_active_bright
    on_press: app.navigationdrawer.toggle_state()

<LeftPanel@BoxLayout+Image>
    ##orientation: "vertical"
    padding: dp(7), dp(7)
    source: 'data/images/dots.png'
    allow_stretch: True
    keep_ratio: False
    on_parent:
        self.texture.wrap = 'repeat'
        self.texture.uvsize = self.texture.size
    Image
        source: "atlas://data/default/logo"
        size_hint: 1, None
        height: dp(130)
        mipmap: True
    ScrollView
        GridLayout
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            MenuButton
                id: bt_sched
                text: 'Schedule'
                on_press:load_screen('ScreenSchedule', manager=app.navigation_manager)
            MenuButton
                text: 'Sponsors'
                on_press:load_screen('ScreenSponsor', manager=app.navigation_manager)
            MenuButton
                text: 'Venue'
                on_press:load_screen('ScreenVenue', manager=app.navigation_manager)
            MenuButton
                text: 'OpenSpaces'
                on_press:load_screen('ScreenOpenSpaces', manager=app.navigation_manager)
            MenuButton
                text: 'DevSprints'
                on_press:load_screen('ScreenDevSprints', manager=app.navigation_manager)
            MenuButton
                text: 'Ticket'
                on_press:load_screen('ScreenTicket', manager=app.navigation_manager)
            MenuButton
                text: 'Community'
                on_press:load_screen('ScreenCommunity', manager=app.navigation_manager)
            MenuButton
                down_count: 0
                text: 'Registration'
                on_press: self.down_count += 1
                on_down_count:
                    if args[1] == 5:load_screen(\
                    'ScreenRegister', manager=app.navigation_manager); self.down_count = 0
            MenuButton
                text: 'About'
                on_press:load_screen('ScreenAbout', manager=app.navigation_manager)

<Topic@Label>
    opacity: 0
    canvas.before:
        Color
            rgba: 0, 0, 0, .5
        Rectangle
            texture: self.texture
            size: self.width - dp(50), self.height
            pos: self.x + dp(22), self.y - dp(2)
    font_size: dp(20)
    text_size: self.width - dp(50), self.height
    halign: 'left'
    valign: 'middle'

<TopBar@BoxLayout+Background>
    size_hint: 1, None
    height: dp(45)
    backcolor: app.base_active_color
    ImBut
        color: 1, 1, 1, 1
        source: 'atlas://data/default/hamburger'
        size_hint_x: None
        size_hint_y: 1
        width: self.height
        allow_stretch: True
        on_press: app.navigationdrawer.toggle_state()

    Topic
        id: topic
        text: app.event_name


<RightPanel@RelativeLayout>
    Image
        source: 'data/images/dots.png'
        allow_stretch: True
        keep_ratio: False
        on_parent:
            self.texture.wrap = 'repeat'
            self.texture.uvsize = self.width/2., self.height/2
        #color: 225./255., 225./255., 225./255., 1
    Image
        mipmap: True
        allow_stretch: True
        #color: 1, 1, 1, .03
        color: app.base_active_bright[:3] + [.05]
        source: 'atlas://data/default/circle1'
    BoxLayout
        ##orientation: "vertical"
        TopBar
            id: topbar
        ScreenManager
            on_parent: app.navigation_manager = nav_sm
            id: nav_sm

<NavigationScreen>
    name: 'NavigationScreen'
    on_enter:
        import os
        scr = os.environ.get('PYCONF_STARTUP_SCREEN','ScreenSchedule')
        load_screen(scr, manager=app.navigation_manager)
        right_panel.ids.topbar.ids.topic.opacity=1
    NavigationDrawer
        id: navigationdrawer
        anim_type: 'slide_above_anim'
        on_parent: app.navigationdrawer = navigationdrawer
        LeftPanel
            id: left_panel
        RightPanel
            id: right_panel
            opacity: 1-(self.x/root.right)
''')
