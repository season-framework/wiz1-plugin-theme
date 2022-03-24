wiz = framework.model("wiz")
fs = framework.model("wizfs").use(f"wiz/plugin/.cache")
config = wiz.config.load("wiz")

def nav(menus):
    for menu in menus:
        pt = None
        if 'pattern' in menu: pt = menu['pattern']
        elif 'url' in menu: pt = menu['url']

        if pt is not None:
            if framework.request.match(pt): menu['class'] = 'active'
            else: menu['class'] = ''

        if 'child' in menu:
            menu['show'] = 'show'
            for i in range(len(menu['child'])):
                child = menu['child'][i]
                cpt = None
            
                if 'pattern' in child: cpt = child['pattern']
                elif 'url' in child: cpt = child['url']

                if cpt is not None:
                    if framework.request.match(cpt): 
                        menu['child'][i]['class'] = 'active'
                        menu['show'] = 'show'
                    else: 
                        menu['child'][i]['class'] = ''
    return menus

def simplenav(menus):
    for menu in menus:
        pt = None
        if 'pattern' in menu: pt = menu['pattern']
        elif 'url' in menu: pt = menu['url']

        if pt is not None:
            if framework.request.match(pt): menu['class'] = 'bg-dark text-white'
            else: menu['class'] = ''

    return menus

kwargs['IS_DEV'] = wiz.is_dev()
kwargs['BRANCH'] = wiz.workspace.branch()
kwargs['BRANCHES'] = wiz.workspace.branches()

menus = list(config.get("topmenus", []))
menus.append({"title": "Setting", "url": '/wiz/admin/setting', 'pattern': r'^/wiz/admin/setting' })
kwargs['topmenus'] = simplenav(menus)

try: navdata = fs.read_pickle("nav")
except: navdata = []
kwargs['menus'] = nav(navdata)
active_id = None
for menu in kwargs['menus']:
    if menu['class'] == 'active':
        active_id = menu['id']

if active_id is None:
    kwargs['submenus'] = []
else:
    try: subnavdata = fs.read_pickle("subnav")
    except: subnavdata = dict()

    if active_id in subnavdata:
        subnavdata = subnavdata[active_id]
        kwargs['submenus'] = simplenav(subnavdata)
