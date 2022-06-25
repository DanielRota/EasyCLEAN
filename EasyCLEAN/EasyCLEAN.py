from ddx import dlg, gdb, msg
from ddx.gdb import cad, view
import os
import ewd
import Functions

begin_path = os.path.dirname(__file__)
program_file = ewd.get_project_path()

EasyCLEAN_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))


def load_plugin_messages():
    language = ewd.get_language()[:3]
    message_filename = "EasyCLEAN_{}.msg".format(language)
    message_path = os.path.join(
        EasyCLEAN_ROOT_PATH, '$$config', message_filename)
    if not os.path.exists(message_path):
        # literal message because here the language used is certainly english
        dlg.output_box('WARNING: Choosen language {} is not supported by the plugin, engish is used'.format(
            ewd.get_language()))
        message_filename = "EasyCLEAN_ENG.msg"
        message_path = os.path.join(
            EasyCLEAN_ROOT_PATH, '$$config', message_filename)
    return msg.MessageManager(message_path)


EasyCLEAN_messages = load_plugin_messages()


class ClassDialog(dlg.DialogHelper):
    def on_init(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        self.file = program_file
        # Set dialog's resizable
        dlg.set_resizable(dialog_id, is_resizable=False)
        # Set columns
        dlg.set_column_size(dialog_id, 1, 20)
        dlg.set_column_size(dialog_id, 2, 50)
        dlg.set_column_size(dialog_id, 3, 20)
        dlg.set_column_size(dialog_id, 4, 50)
        dlg.set_column_size(dialog_id, 5, 50)
        dlg.set_column_size(dialog_id, 6, 30)
        dlg.set_column_size(dialog_id, 7, 50)
        dlg.set_column_size(dialog_id, 8, 60)
        dlg.set_column_size(dialog_id, 9, 60)
        dlg.set_column_size(dialog_id, 10, 10)
        dlg.set_column_size(dialog_id, 11, 20)
        dlg.set_column_size(dialog_id, 12, 55)
        dlg.set_column_size(dialog_id, 13, 20)
        # Set rows
        dlg.set_row_size(dialog_id, 1, 120)
        dlg.set_row_size(dialog_id, 2, 50)
        dlg.set_row_size(dialog_id, 3, 30)
        dlg.set_row_size(dialog_id, 4, 25)
        dlg.set_row_size(dialog_id, 5, 25)
        dlg.set_row_size(dialog_id, 6, 20)
        dlg.set_row_size(dialog_id, 7, 50)
        dlg.set_row_size(dialog_id, 8, 50)
        dlg.set_row_size(dialog_id, 9, 50)
        dlg.set_row_size(dialog_id, 10, 20)

        # Add widgets
        dlg.add_widget(dialog_id, "LOGO", dlg.WidgetType.IMAGE,
                       begin_path + "\\Images\\Logo.png", row=1, col=1, col_span=13)
        dlg.add_widget(dialog_id, "SEARCH", dlg.WidgetType.BUTTON,
                       "", col=1, row=2, row_span=1, col_span=2)
        dlg.add_widget(dialog_id, "RESTART", dlg.WidgetType.BUTTON,
                       "", col=3, row=2, row_span=1, col_span=2)
        dlg.add_widget(dialog_id, "EXPORT", dlg.WidgetType.BUTTON,
                       "", col=5, row=2, row_span=1, col_span=2)
        dlg.add_widget(dialog_id, "LABEL", dlg.WidgetType.LABEL, EasyCLEAN_messages.get_msg(
            1), col=7, row=2, row_span=1, col_span=3)
        dlg.add_widget(dialog_id, "STATO", dlg.WidgetType.LABEL, EasyCLEAN_messages.get_msg(
            2), col=9, row=2, row_span=1, col_span=4)
        dlg.add_widget(dialog_id, "LINEA", dlg.WidgetType.IMAGE,  begin_path +
                       "\\Images\\Barra.png", col=1, row=3, row_span=1, col_span=13)
        dlg.add_widget(dialog_id, "HIDE", dlg.WidgetType.BUTTON, EasyCLEAN_messages.get_msg(
            3), col=1, row=4, row_span=2, col_span=4)
        dlg.add_widget(dialog_id, "DELETE", dlg.WidgetType.BUTTON, EasyCLEAN_messages.get_msg(
            4), col=10, row=4, row_span=2, col_span=3)
        dlg.add_widget(dialog_id, "CHECK1", dlg.WidgetType.CHECK,
                       True, col=8, row=4, row_span=1, col_span=2)
        dlg.add_widget(dialog_id, "CHECK2", dlg.WidgetType.CHECK,
                       True, col=6, row=4, row_span=1, col_span=2)
        dlg.add_widget(dialog_id, "CHECK3", dlg.WidgetType.CHECK,
                       True, col=8, row=5, row_span=1, col_span=2)
        dlg.add_widget(dialog_id, "CHECK4", dlg.WidgetType.CHECK,
                       True, col=6, row=5, row_span=1, col_span=2)
        dlg.add_widget(dialog_id, "ORIGIN", dlg.WidgetType.BUTTON, EasyCLEAN_messages.get_msg(
            5), col=1, row=7, row_span=1, col_span=4)
        dlg.add_widget(dialog_id, "AXIS", dlg.WidgetType.BUTTON, EasyCLEAN_messages.get_msg(
            31), col=5, row=7, row_span=1, col_span=3)
        dlg.add_widget(dialog_id, "SHAPE", dlg.WidgetType.BUTTON, EasyCLEAN_messages.get_msg(
            6), col=1, row=8, row_span=1, col_span=7)
        dlg.add_widget(dialog_id, "SHARP", dlg.WidgetType.BUTTON, EasyCLEAN_messages.get_msg(
            7), col=1, row=9, row_span=1, col_span=7)
        dlg.add_widget(dialog_id, "SCENE", dlg.WidgetType.SCENE,
                       "", col=8, row=7, row_span=3, col_span=5)

        # Set widget enable
        dlg.set_widget_enable(dialog_id, "DELETE", enable=True)
        dlg.set_widget_enable(dialog_id, "CHECK1", enable=True)
        dlg.set_widget_enable(dialog_id, "CHECK2", enable=True)
        dlg.set_widget_enable(dialog_id, "CHECK3", enable=True)
        dlg.set_widget_enable(dialog_id, "CHECK4", enable=True)
        dlg.set_widget_enable(dialog_id, "SHAPE", enable=False)
        dlg.set_widget_enable(dialog_id, "ORIGIN", enable=True)
        dlg.set_widget_enable(dialog_id, "EXPORT", enable=False)
        dlg.set_widget_enable(dialog_id, "SHARP", enable=False)
        if self.file == "":
            dlg.set_widget_enable(dialog_id, "RESTART", enable=False)

        # Set button icons
        dlg.set_widget_property(
            dialog_id, "SEARCH", 'ICON', begin_path + "\\Images\\AddDocument.png")
        dlg.set_widget_property(dialog_id, "HIDE", 'ICON',
                                begin_path + "\\Images\\HideMember.png")
        dlg.set_widget_property(dialog_id, "RESTART",
                                'ICON', begin_path + "\\Images\\Restart.png")
        dlg.set_widget_property(dialog_id, "DELETE",
                                'ICON', begin_path + "\\Images\\Delete.png")
        dlg.set_widget_property(
            dialog_id, "ORIGIN", 'ICON', begin_path + "\\Images\\AddNoColor.png")
        dlg.set_widget_property(
            dialog_id, "SHAPE", 'ICON', begin_path + "\\Images\\BorderElement.png")
        dlg.set_widget_property(dialog_id, "EXPORT", 'ICON',
                                begin_path + "\\Images\\Export.png")
        dlg.set_widget_property(dialog_id, "AXIS", 'ICON',
                                begin_path + "\\Images\\AxisY.png")
        dlg.set_widget_property(
            dialog_id, "ORIGIN", 'ICON', begin_path + "\\Images\\AddNoColor.png")
        dlg.set_widget_property(
            dialog_id, "SHARP", 'ICON', begin_path + "\\Images\\Saw_black.png")
        dlg.set_widget_property(
            dialog_id, "SCENE", dlg.WidgetProp.SCENE_MODALITY_VIEW, "")

        # Set icons style
        dlg.set_widget_property(dialog_id, "HIDE", 'ICON_ALIGN', 'LEFT')
        dlg.set_widget_property(dialog_id, "ORIGIN", 'ICON_ALIGN', 'LEFT')
        dlg.set_widget_property(dialog_id, "DELETE", 'ICON_ALIGN', 'LEFT')
        dlg.set_widget_property(dialog_id, "SHAPE", 'ICON_ALIGN', 'LEFT')
        dlg.set_widget_property(dialog_id, "EXPORT", 'ICON_ALIGN', 'LEFT')
        dlg.set_widget_property(dialog_id, "ORIGIN", 'ICON_ALIGN', 'LEFT')
        dlg.set_widget_property(dialog_id, "CHECK1",
                                'CHECK_TEXT', EasyCLEAN_messages.get_msg(8))
        dlg.set_widget_property(dialog_id, "CHECK2",
                                'CHECK_TEXT', EasyCLEAN_messages.get_msg(9))
        dlg.set_widget_property(dialog_id, "CHECK3",
                                'CHECK_TEXT', EasyCLEAN_messages.get_msg(10))
        dlg.set_widget_property(dialog_id, "CHECK4",
                                'CHECK_TEXT', EasyCLEAN_messages.get_msg(11))

        # Set widgets TOOLTIP
        dlg.set_widget_property(
            dialog_id, "EXPORT", dlg.WidgetProp.TOOLTIP, EasyCLEAN_messages.get_msg(12))
        dlg.set_widget_property(
            dialog_id, "SEARCH", dlg.WidgetProp.TOOLTIP, EasyCLEAN_messages.get_msg(13))
        dlg.set_widget_property(
            dialog_id, "RESTART", dlg.WidgetProp.TOOLTIP, EasyCLEAN_messages.get_msg(14))
        dlg.set_widget_property(
            dialog_id, "HIDE", dlg.WidgetProp.TOOLTIP, EasyCLEAN_messages.get_msg(15))
        dlg.set_widget_property(
            dialog_id, "DELETE", dlg.WidgetProp.TOOLTIP, EasyCLEAN_messages.get_msg(16))
        dlg.set_widget_property(
            dialog_id, "ORIGIN", dlg.WidgetProp.TOOLTIP, EasyCLEAN_messages.get_msg(17))
        dlg.set_widget_property(
            dialog_id, "SHAPE", dlg.WidgetProp.TOOLTIP, EasyCLEAN_messages.get_msg(18))
        dlg.set_widget_property(
            dialog_id, "SHARP", dlg.WidgetProp.TOOLTIP, EasyCLEAN_messages.get_msg(19))

        # set scene visible
        dlg.set_widget_visible(dialog_id, "SCENE", visible=False)

        # Set logo
        dlg.set_widget_style(
            dialog_id, "LOGO", dlg.WidgetStyle.EXPAND, width=200, height=60)

        dlg.show_ok_cancel(dialog_id, False)

        return True

    def on_click_SEARCH(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        self.file = dlg.select_file(
            "dwg files (*.dwg)|*.dwg|dxf files (*.dxf)|*.dxf", "", open_file=True, select_multiple=False)
        if self.file != "":
            dlg.set_widget_enable(dialog_id, "HIDE", enable=True)
            ewd.open_project(self.file)
            dlg.set_widget_value(dialog_id, "STATO",
                                 EasyCLEAN_messages.get_msg(20))
            dlg.set_widget_enable(dialog_id, "RESTART", enable=True)
            dlg.set_widget_enable(dialog_id, "DELETE", enable=True)
            dlg.set_widget_enable(dialog_id, "ORIGIN", enable=True)
            dlg.set_widget_enable(dialog_id, "CHECK1", enable=True)
            dlg.set_widget_enable(dialog_id, "CHECK2", enable=True)
            dlg.set_widget_enable(dialog_id, "CHECK3", enable=True)
            dlg.set_widget_enable(dialog_id, "CHECK4", enable=True)
            dlg.set_widget_enable(dialog_id, "SHAPE", enable=False)
            dlg.set_widget_enable(dialog_id, "EXPORT", enable=False)
            dlg.set_widget_visible(dialog_id, "SCENE", visible=False)
            dlg.set_widget_enable(dialog_id, "AXIS", enable=True)
            dlg.set_widget_value(dialog_id, "SCENE", "")
            dlg.set_widget_enable(dialog_id, "SHARP", enable=False)
        return True

    def on_click_RESTART(self, dialog_id, widget_id, widget_key, event_id, widget_type):

        ewd.open_project(self.file)

        dlg.set_widget_enable(dialog_id, "RESTART", enable=True)
        dlg.set_widget_enable(dialog_id, "DELETE", enable=True)
        dlg.set_widget_enable(dialog_id, "ORIGIN", enable=True)
        dlg.set_widget_enable(dialog_id, "CHECK1", enable=True)
        dlg.set_widget_enable(dialog_id, "CHECK2", enable=True)
        dlg.set_widget_enable(dialog_id, "CHECK3", enable=True)
        dlg.set_widget_enable(dialog_id, "CHECK4", enable=True)
        dlg.set_widget_enable(dialog_id, "SHAPE", enable=False)
        dlg.set_widget_enable(dialog_id, "HIDE", enable=True)
        dlg.set_widget_enable(dialog_id, "AXIS", enable=True)
        dlg.set_widget_value(dialog_id, "STATO",
                             EasyCLEAN_messages.get_msg(21))
        dlg.set_widget_enable(dialog_id, "EXPORT", enable=False)
        dlg.set_widget_enable(dialog_id, "SHARP", enable=False)
        dlg.set_widget_visible(dialog_id, "SCENE", visible=False)
        dlg.set_widget_value(dialog_id, "SCENE", "")
        return True

    def on_click_HIDE(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        if gdb.get_selection_count() > 0:
            dlg.set_widget_property(dialog_id, "STATO", 'CHECK_TEXT', 'TESTI')
            dlg.set_widget_enable(dialog_id, "CHECK1", enable=True)
            dlg.set_widget_enable(dialog_id, "CHECK2", enable=True)
            dlg.set_widget_enable(dialog_id, "CHECK3", enable=True)
            dlg.set_widget_enable(dialog_id, "CHECK4", enable=True)
            dlg.set_widget_enable(dialog_id, "DELETE", enable=True)
            dlg.set_widget_enable(dialog_id, "ORIGIN", enable=True)
            self.all_entities = Functions.hide_useles()
            dlg.set_widget_value(dialog_id, "STATO",
                                 EasyCLEAN_messages.get_msg(22))
        else:
            dlg.output_box(EasyCLEAN_messages.get_msg(23))
        view.redraw_window()
        return True

    def controllo(self, dialog_id):
        stato1 = dlg.get_widget_value(dialog_id, "CHECK1")
        stato2 = dlg.get_widget_value(dialog_id, "CHECK2")
        stato3 = dlg.get_widget_value(dialog_id, "CHECK3")
        stato4 = dlg.get_widget_value(dialog_id, "CHECK4")
        if str(stato1) == "0" and str(stato2) == "0" and str(stato3) == "0" and str(stato4) == "0":
            dlg.set_widget_enable(dialog_id, "DELETE", enable=False)
        else:
            dlg.set_widget_enable(dialog_id, "DELETE", enable=True)

    def on_click_CHECK1(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        dlg.set_widget_enable(dialog_id, "DELETE", enable=True)
        self.controllo(dialog_id)
        return True

    def on_click_CHECK2(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        dlg.set_widget_enable(dialog_id, "DELETE", enable=True)
        self.controllo(dialog_id)
        return True

    def on_click_CHECK3(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        dlg.set_widget_enable(dialog_id, "DELETE", enable=True)
        self.controllo(dialog_id)
        return True

    def on_click_CHECK4(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        dlg.set_widget_enable(dialog_id, "DELETE", enable=True)
        self.controllo(dialog_id)
        return True

    def on_click_DELETE(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        checked = [dlg.get_widget_value(dialog_id, "CHECK2"), dlg.get_widget_value(
            dialog_id, "CHECK3"), dlg.get_widget_value(dialog_id, "CHECK4"), dlg.get_widget_value(dialog_id, "CHECK1")]
        array = []
        for item in checked:
            if str(item) == "1":
                array.append(True)
            else:
                array.append(False)
        Functions.clear_main_area(array)
        dlg.set_widget_enable(dialog_id, "ORIGIN", enable=True)
        dlg.set_widget_value(dialog_id, "STATO",
                             EasyCLEAN_messages.get_msg(24))
        view.redraw_window()
        return True

    def on_click_ORIGIN(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        self.origin_line = Functions.get_origin_line()
        if self.origin_line != None:
            dlg.set_widget_enable(dialog_id, "SHAPE", enable=True)
            dlg.set_widget_value(dialog_id, "STATO",
                                 EasyCLEAN_messages.get_msg(25))
            view.redraw_window()
        else:
            dlg.output_box(EasyCLEAN_messages.get_msg(26))
        return True
    
    def on_click_AXIS(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        Functions.get_axis(self.origin_line)
        return True

    def on_click_SHAPE(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        dlg.set_widget_enable(dialog_id, "CHECK1", enable=False)
        dlg.set_widget_enable(dialog_id, "CHECK2", enable=False)
        dlg.set_widget_enable(dialog_id, "CHECK3", enable=False)
        dlg.set_widget_enable(dialog_id, "CHECK4", enable=False)
        dlg.set_widget_enable(dialog_id, "DELETE", enable=False)
        dlg.set_widget_enable(dialog_id, "ORIGIN", enable=False)
        dlg.set_widget_enable(dialog_id, "ORIGIN", enable=False)
        dlg.set_widget_enable(dialog_id, "AXIS", enable=False)
        self.shape_layer, self.origin_point, self.origin_line, self.origin_max = Functions.get_shape(
            self.origin_line)
        dlg.set_widget_visible(dialog_id, "SCENE", visible=True)
        lay = []
        part = cad.get_current_part()
        lay = part + "\\ShapeLay"

        
        
        # set scene property
        # T for Top view, A for zoom including All object loaded in the scene,
        # 2 for fixed 2d grid (user is no longer able to rotate the scene)
        
        view.redraw_window()
        dlg.set_widget_enable(dialog_id, "SHARP", enable=True)
        dlg.set_widget_value(dialog_id, "STATO",
                             EasyCLEAN_messages.get_msg(27))
        dlg.set_widget_enable(dialog_id, "EXPORT", enable=True)
        part = cad.get_current_part()
        lay = part + "\\ShapeLay"
        lays = cad.get_layers(part=None)
        for item in lays:
            item = part + "\\" + item
            if item != lay:
                gdb.delete_layer(item)
        Functions.mirror_move(self.shape_layer, self.origin_point, self.origin_line, self.origin_max)
        gdb.reset_selection()
        ewd.zoom_all()
        self.temp = ewd.explode_file_path("%TEMPPATH%\\temp.ewd")
        gdb.export_file(self.temp, lay)
        dlg.set_widget_value(dialog_id, "SCENE", self.temp)
        dlg.set_widget_property(dialog_id, "SCENE", 'VIEW', "TA2")
        dlg.set_widget_enable(dialog_id, "SHAPE", enable=False)
        return True

    def on_click_EXPORT(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        part = cad.get_current_part()
        #lay = part + "\\ShapeLay"
        self.new_file = dlg.select_file("ewd files (*.ewd)|*.ewd", initial_dir='', open_file=False, select_multiple=False)
        #ewd.EXPORT_project(self.new_file)
        gdb.export_file(self.new_file, part)
        dlg.set_widget_value(dialog_id, "STATO",EasyCLEAN_messages.get_msg(28))
        dlg.set_widget_value(dialog_id, "SCENE", self.new_file)
        dlg.set_widget_property(dialog_id, "SCENE", 'VIEW', "TA2")      
        return True

    def on_click_SHARP(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        if Functions.color_sharp():
            dlg.set_widget_value(dialog_id, "STATO",
                                 EasyCLEAN_messages.get_msg(29))
        else:
            dlg.output_box(EasyCLEAN_messages.get_msg(30))
        view.redraw_window()

    def on_right_click_SHARP(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        sharp = gdb.get_selection()
        for entity in sharp:
            cad.set_material(entity, cad.StandardColors.BLUE_DARK)
        view.redraw_window()

    def on_cancel(self, dialog_id, widget_id, widget_key, event_id, widget_type):
        dlg.end_modal_dialog(dialog_id)
        return True


if __name__ == '__main__':
    ClassDialog(title="EasyCLEAN", size=(500, 470),
                mode=dlg.DialogMode.MODLESS).run()
