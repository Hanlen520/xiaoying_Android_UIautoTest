#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Public.BasePage import BasePage
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError

class Edit_Page(BasePage):
    @teststep
    def select_editor_tab(self, inst=1):
        '''
        切换编辑模块，主题、编辑、效果
        :param inst:1主题；2编辑；3效果
        '''
        self.d(className="android.support.v7.app.ActionBar$b",instance=inst-1).click()

    @teststep
    def click_draft_btn(self):
        '''点击存草稿'''
        self.d(resourceId="com.quvideo.xiaoying:id/editor_draft").click()

    @teststep
    def click_publish_btn(self):
        '''点击发布按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/editor_publish").click()

    @teststep
    def click_back_btn(self):
        '''点击返回按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/editor_back_btn").click()

    @teststep
    def click_seekbar_play_btn(self):
        '''点击播放按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/seekbar_play").click()


    @teststep
    def get_seekabr_time(self):
        '''获取seekbar的播放时长和视频总时长'''
        cur_time = self.d(resourceId="com.quvideo.xiaoying:id/txtview_cur_time").get_text()
        total_time = self.d(resourceId="com.quvideo.xiaoying:id/txtview_duration").get_text()
        return cur_time, total_time

    @teststep
    def select_seekbar_position(self, inst=5):
        '''
        点击seekbar的播放位置
        :param inst: inst  [0~10)之间任意数字  exp 0.2、0.4、...1.8、2.0
        '''
        bar = self.d(resourceId="com.quvideo.xiaoying:id/seekbar_simple_edit").info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 10
        x = bar['left'] + inst * unit
        self.d.long_click(x, y)

    @teststep
    def click_add_clip_bt(self):
        '''点击添加clip按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/clipedit_add_btn").click()

    @teststep
    def select_clip_edit_tool(self, text="滤镜"):
        '''点击镜头编辑功能位'''
        self.d(resourceId="com.quvideo.xiaoying:id/clipedit_tool_rcview", scrollable=True).scroll.horiz.to(text=text)
        if self.d(text=text).exists:
            self.d(text=text).click()
            return True
        else:
            print("找不到编辑控件-->%s" % text)
            return False

    @teststep
    def select_effect_edit_tool(self, text="字幕"):
        '''点击镜头编辑功能位'''
        self.d(resourceId="com.quvideo.xiaoying:id/effect_tool_rcview", scrollable=True).scroll.horiz.to(text=text)
        if self.d(text=text).exists:
            self.d(text=text).click()
            return True
        else:
            print("找不到效果控件-->%s" % text)
            return False

    @teststep
    def select_theme(self, text="无主题"):
        '''点击镜头编辑功能位'''
        self.d(resourceId="com.quvideo.xiaoying:id/rv_theme_editor", scrollable=True).scroll.horiz.to(text=text)
        if self.d(text=text).exists:
            self.d(text=text).click()
            return True
        else:
            print("找不到主题-->%s" % text)
            return False

    @teststep
    def click_change_music_btn(self):
        '''点击主题下 更换配乐按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/rv_theme_editor", scrollable=True).scroll.horiz.\
            to(resourceId="com.quvideo.xiaoying:id/tv_theme_change_music")
        if self.d(resourceId="com.quvideo.xiaoying:id/tv_theme_change_music").exists:
            self.d(resourceId="com.quvideo.xiaoying:id/tv_theme_change_music").click()
            return True
        else:
            print("找不到修改配乐按钮")
            return False

    @teststep
    def click_effect_play_btn(self):
        '''点击效果页面的播放按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_play").click()

    @teststep
    def get_effect_seek_time(self):
        '''获取效果页面的播放时长和视频总时长'''
        cur_time = self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_current_time").get_text()
        total_time = self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_duration").get_text()
        return cur_time, total_time

    @teststep
    def preview_swipe_left(self):
        ele = self.d(resourceId="com.quvideo.xiaoying:id/preview_layout")
        BasePage().swipe_left(ele)

    @teststep
    def preview_swipe_right(self):
        ele = self.d(resourceId="com.quvideo.xiaoying:id/preview_layout")
        BasePage().swipe_right(ele)

    @teststeps
    def delete_clip(self, inst=1):
        '''删除clip'''
        self.d(resourceId="com.quvideo.xiaoying:id/item_delete_btn", instance=inst-1).click()
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive").click()

    @teststep
    def click_transition_btn(self, inst=1):
        '''点击clipsbar中的转场按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/transition_entrance_btn", instance=inst-1).click()

    @teststep
    def click_clip(self,inst=1):
        '''点击 clip'''
        self.d(resourceId="com.quvideo.xiaoying:id/item_comtent",  instance=inst-1).click()

    @teststep
    def drag_clip(self, start=1, end=2):
        '''
        拖动clipboard上clip的顺序
        :param start: 被移动clips的顺序
        :param end:  移动到clips的位置顺序
        :return:
        '''
        start_clip = self.d(resourceId="com.quvideo.xiaoying:id/item_cover", instance=start - 1)
        # start.click()
        end_clip = self.d(resourceId="com.quvideo.xiaoying:id/item_cover", instance=end - 1).info["bounds"]
        if start > end:
            start_clip.drag_to(end_clip["left"], end_clip["top"])
        else:
            start_clip.drag_to(end_clip["right"], end_clip["bottom"])
        print(end)

    @teststep
    def effect_setting(self):
        '''设定生效按钮点击'''
        self.d(resourceId="com.quvideo.xiaoying:id/terminator_right").click()

    @teststeps
    def cancel_setting(self):
        '''设定取消操作'''
        self.d(resourceId="com.quvideo.xiaoying:id/terminator_left").click()
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive").click_exists(timeout=1)








if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    # Edit_Page().select_seekbar_position(5)
    # Edit_Page().select_effect_edit_tool("配音和音效")
    # Edit_Page().click_effect_play_btn()
    # print(Edit_Page().get_effect_seek_time())
    # Edit_Page().preview_swipe_left()
    # Edit_Page().preview_swipe_right()
    # Edit_Page().click_clip(1)
    # Edit_Page().select_clip_edit_tool("镜头排序")
    # Edit_Page().drag_clip(1, 8)
    Edit_Page().cancel_setting()
