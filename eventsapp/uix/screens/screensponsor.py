'''ScreenSponsor:
Display all the logos of the sponsors.
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from network import get_data
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout


class Sponsor(BoxLayout):
    ''' This is a simple StackLayout that holds the image
    '''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.data = kwargs["data"]

    data = ObjectProperty(None)


class ScreenSponsor(Screen):

    Builder.load_string('''
<ScreenSponsor>
    name: 'ScreenSponsor'
    BoxLayout
        #orientation: "vertical"
        BackLabel
            text: "Sponsors"
            backcolor: app.base_inactive_color[:3] + [.5]
            pos_hint:{'top':1}
            size_hint: 1 , None
            height: dp(10)
            font_size:dp(20)
        ScrollView
            GridLayout
                cols: 1
                #orientation: 'vertical'
                spacing: dp(4)
                size_hint_y: None
                height: self.minimum_height
                id: main
        Footer
<Footer@BoxLayout>
    size_hint_y: None
    padding: dp(9)
    spacing: dp(9)
    height: dp(54)
    ActiveButton
        text: 'Sponsor Us'
        size_hint_y: None
        height: dp(40)
        on_release:
            import webbrowser
            webbrowser.open(\
            'https://in.pycon.org/2018/sponsorship_prospectus.pdf')
    ActiveButton
        text: 'Contact Us'
        size_hint_y: None
        height: dp(40)
        on_release:
            import webbrowser
            webbrowser.open('mailto:sponsorship@in.pycon.org')

<Sponsor>
    #orientation: 'vertical'
    spacing: dp(12)
    size_hint: 1, None
    height: dp(120)
    BackLabel
        text: self.parent.data['name']
        size_hint: 1, None
        height: dp(20)
        font_size:dp(18)
    SponsorImage
        data: {"logo":"fff"}
        on_release:
            import webbrowser
            webbrowser.open(root.data['website'])

<SponsorImage@ButtonBehavior+AsyncImage>
    size_hint:1,.8
    halign: 'center'
    padding: dp(10), dp(10)
    valign: 'middle'
    allow_stretch:False
    source: self.parent.data['logo']
    on_release:
        import webbrowser
        print("---self.parent.data",self.parent.data)
        webbrowser.open(self.parent.data['website'])

''')

    def on_enter(self, onsuccess=False):
        '''Series of actions to be performed when Schedule screen is entered
        '''

        # this should update the file on disk
        sponsors = get_data('sponsors', onsuccess=onsuccess)
        if not sponsors:
            return

        sponsors = sponsors.get('0.0.1')
        main_box = self.ids.main
        #main_box.clear_widgets()
        for s in sponsors:
            print(s)
            bl = Factory.Sponsor(size_hint_y=.8/len(sponsors), data=s)
            self.data = s
            main_box.add_widget(bl)
        # footer = Factory.Footer()
        # main_box.add_widget(footer)
