from libqtile import widget
from settings.theme import colors

# iconos en https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=13, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=1
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=30,
        padding=-2,
)

# Widgets de grupos de trabajos, en iconos  
def workspaces(): 
    return [
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=14,
            margin_y=3,
            margin_x=-1,
            padding_y=0,
            padding_x=0,
            borderwidth=0,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=11, padding=2),
        separator(),

    ]

primary_widgets = [
    *workspaces(),

    separator(),

    #widgets de actualizaciones
    powerline('color4', 'dark'),

    icon(bg="color4", text=' ', fontsize = 12), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0 ',
        display_format='{updates} ',
        update_interval=1800,
        custom_command='checkupdates',
        fontsize=11
    ),
	
	# Widget de Red 	
    powerline('color3', 'color4'),

    icon(bg="color3", text=' ', fontsize = 12),  # Icon: nf-fa-feed
    
    widget.Net(**base(bg='color3'), interface='wlo1', fontsize = 11, format = '{interface}: {down} ↓↑ {up} ',),

    # Widget de calendario
    powerline('color2', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5, fontsize=11),

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=13, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %I:%M %p ', fontsize = 11),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=6, icon_size = 10),
]

#Widgets de fechas
secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

# default widget, fuentes, tamano estandar de los widgets 
widget_defaults = {
    'font': 'UbuntuMono Nerd Font ',
    'fontsize': 10,
    'padding': 0,
}
extension_defaults = widget_defaults.copy()
