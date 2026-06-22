translate chinese python:
    #游戏内对话文本字体
    gui.text_font = "tl/chinese/fonts/SourceHanSansCN-Bold.ttf"
    #游戏内人物角色名称字体
    gui.name_text_font = "tl/chinese/fonts/KNMaiyuan-Regular.ttf"
    #设置页面字体
    gui.interface_text_font = "tl/chinese/fonts/MiSans-Bold.ttf"
    #系统设置字体
    gui.button_text_font = gui.interface_text_font
    #游戏内选项文本字体
    gui.choice_button_text_font = gui.text_font
    #系统默认字体
    gui.system_font = "tl/chinese/fonts/MiSans-Regular.ttf"

    # 将 acme 字体名称映射到 MiSans-Bold，覆盖所有硬编码 font 'acme' 的样式
    # 这比逐个设置 style.X.font 更可靠，因为 config.font_name_map 必定存在
    config.font_name_map['acme'] = "tl/chinese/fonts/MiSans-Bold.ttf"