#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Public.BasePage import BasePage
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class edit_page(BasePage):
    # ————————————————————————
    # 主题、镜头编辑、素材效果公共方法
    # ————————————————————————
    @teststep
    def select_editor_tab(self, inst=1):
        '''
        切换编辑模块，主题、编辑、效果
        :param inst:1主题；2编辑；3效果
        '''
        self.d(className="android.support.v7.app.ActionBar$b", instance=inst - 1).click()

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
        cur = self.d(resourceId="com.quvideo.xiaoying:id/txtview_cur_time").get_text().split(":")
        cur_time = float(cur[0]) * 60 + float(cur[1])
        total = self.d(resourceId="com.quvideo.xiaoying:id/txtview_duration").get_text().split(":")
        total_time = float(total[0]) * 60 + float(total[1])
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
    def effect_setting(self):
        '''设定生效按钮点击'''
        self.d(resourceId="com.quvideo.xiaoying:id/terminator_right").click()

    @teststeps
    def cancel_setting(self):
        '''设定取消操作'''
        self.d(resourceId="com.quvideo.xiaoying:id/terminator_left").click()
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive").click_exists(timeout=1)

    @teststep
    def preview_swipe_left(self):
        '''预览页右滑动'''
        ele = self.d(resourceId="com.quvideo.xiaoying:id/preview_layout")
        BasePage().swipe_left(ele)

    @teststep
    def preview_swipe_right(self):
        '''预览页左滑动'''
        ele = self.d(resourceId="com.quvideo.xiaoying:id/preview_layout")
        BasePage().swipe_right(ele)

    # ————————————————————————
    # 镜头编辑页面方法
    # ————————————————————————
    @teststep
    def click_apply_all_btn(self):
        '''点击应用全部镜头'''
        self.d(resourceId="com.quvideo.xiaoying:id/apply_all_layout").click()

    @teststep
    def get_clip_time(self, inst=1):
        '''
        获取缩略图内的时间
        :param inst: 存在时间显示的clip缩略图，不包含 focus状态的clip
        :return:
        '''
        str_time = self.d(resourceId="com.quvideo.xiaoying:id/item_duration", instance=inst - 1).get_text().split(":")
        clip_time = float(str_time[0]) * 60 + float(str_time[1])
        return clip_time

    # def is_focused(self,inst=1):
    #     focused = self.d(resourceId="com.quvideo.xiaoying:id/item_comtent", instance=inst-1).\
    #         child(resourceId="com.quvideo.xiaoying:id/item_focus_layout").exists
    #     return focused

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

    @teststeps
    def delete_clip(self, inst=1):
        '''删除clip'''
        self.d(resourceId="com.quvideo.xiaoying:id/item_delete_btn", instance=inst - 1).click()
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive").click()

    @teststep
    def click_transition_btn(self, inst=1):
        '''点击clipsbar中的转场按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/transition_entrance_btn", instance=inst - 1).click()

    @teststep
    def click_clip(self, inst=1):
        '''点击 clip'''
        self.d(resourceId="com.quvideo.xiaoying:id/item_comtent", instance=inst - 1).click()

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

    # ————————————————————————
    # 素材效果页面方法
    # ————————————————————————
    @teststep
    def select_effect_edit_tool(self, text="字幕"):
        '''点击素材效果功能位'''
        self.d(resourceId="com.quvideo.xiaoying:id/effect_tool_rcview", scrollable=True).scroll.horiz.to(text=text)
        if self.d(text=text).exists:
            self.d(text=text).click()
            return True
        else:
            print("找不到效果控件-->%s" % text)
            return False

    @teststep
    def click_effect_play_btn(self):
        '''点击效果页面的播放按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_play").click()

    @teststep
    def get_effect_seek_time(self):
        '''获取效果页面的播放时长和视频总时长'''
        cur = self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_current_time").get_text().split(":")
        cur_time = float(cur[0]) * 60 + float(cur[1])
        total = self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_duration").get_text().split(":")
        total_time = float(total[0]) * 60 + float(total[1])
        return cur_time, total_time

    @teststep
    def effect_view_swipe_left(self):
        '''素材效果页seekbar左滑'''
        ele = self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_gallery")
        BasePage().swipe_left(ele)

    @teststep
    def effect_view_swipe_rigth(self):
        '''素材效果页seekbar右滑'''
        ele = self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_gallery")
        BasePage().swipe_right(ele)

    # ————————————————————————
    # 主题配乐页面方法
    # ————————————————————————
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
        self.d(resourceId="com.quvideo.xiaoying:id/rv_theme_editor", scrollable=True).scroll.horiz. \
            to(resourceId="com.quvideo.xiaoying:id/tv_theme_change_music")
        if self.d(resourceId="com.quvideo.xiaoying:id/tv_theme_change_music").exists:
            self.d(resourceId="com.quvideo.xiaoying:id/tv_theme_change_music").click()
            return True
        else:
            print("找不到修改配乐按钮")
            return False


class fitler_page(BasePage):
    '''滤镜操作页面'''

    @teststep
    def select_filter(self, text="原图"):
        '''选择滤镜卷，并点击展开滤镜卷'''
        ele = self.d(resourceId="com.quvideo.xiaoying:id/rc_editor_filter")
        BasePage().find_element_by_swipe_left(self.d(text=text), ele, max_swipe=15)
        time.sleep(1)
        self.d(resourceId="com.quvideo.xiaoying:id/item_fitler_parent_name", text=text).click()
        time.sleep(3)  # 等待下载完成

    @teststeps
    def click_filter_btn(self, text):
        '''点击选择滤镜'''
        ele = self.d(resourceId="com.quvideo.xiaoying:id/rc_editor_filter")
        BasePage().find_element_by_swipe_left(self.d(text=text), ele)
        time.sleep(1)  # 等待主题馆展开
        self.d(resourceId="com.quvideo.xiaoying:id/item_fitler_child_name", text=text).click()

    @teststeps
    def select_filter_alpha(self, inst=50):
        '''
        设置滤镜程度 除了（0~10） 之间的的任意数字,5左右的数字存在一定的偏差
        :param inst: inst  0—~104之间任意间隔0.2的数字  exp 1。2、0.4、...1.8、9.8
        '''
        bar = self.d(resourceId="com.quvideo.xiaoying:id/indicatorSeekBar").info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 120
        x = 10 * unit + bar['left'] + inst * unit
        print(bar)
        print(x, y)
        self.d.long_click(x, y)


class scale_page(BasePage):
    '''比例和背景操作页面'''

    @teststep
    def click_fit_btn(self):
        '''点击缩放按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/iv_btn_fit").click()

    @teststep
    def click_play_btn(self):
        '''点击播放按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/ib_play").click()

    @teststeps
    def select_scale(self, text="1:1"):
        '''
        选择画面比例
        :param text: 比例对应的文字 例如 4:3  注意冒号
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/hs_clip_ratios", scrollable=True).scroll.horiz.to(text=text)
        self.d(resourceId="com.quvideo.xiaoying:id/ratio_title", text=text).click()

    @teststep
    def pinch_view(self, mode="in"):
        '''缩放预览窗口'''
        self.d(resourceId="com.quvideo.xiaoying:id/video_editor_preview").wait()
        if mode == "in":
            self.d(resourceId="com.quvideo.xiaoying:id/video_editor_preview").pinch_in(percent=13, steps=10)
        elif mode == "out":
            self.d(resourceId="com.quvideo.xiaoying:id/video_editor_preview").pinch_out(percent=66, steps=10)

    @teststep
    def select_blur_alpha(self, inst=50):
        '''
        设置背景模糊程度
        :param inst: [0:99) 任意数字
        :return:
        '''
        bar = self.d(resourceId="com.quvideo.xiaoying:id/seekbar_blur").info['bounds']
        y = (bar['bottom'] + bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 100
        x = bar['left'] + inst * unit
        self.d.long_click(x, y)

    @teststep
    def select_colour(self, inst=14):
        '''
        设置背景颜色
        :param inst:[1:28]任意整数
        :return:
        '''
        bar = self.d(resourceId="com.quvideo.xiaoying:id/multicolor_bar").info['bounds']
        y = (bar['bottom'] + bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 28
        x = bar['left'] + inst * unit - 4
        self.d.long_click(x, y)

    @teststep
    def select_backpic_blur_alpha(self, inst=50):
        '''
        设置背景模糊程度
        :param inst: [0:99) 任意数字
        :return:
        '''
        bar = self.d(resourceId="com.quvideo.xiaoying:id/pic_seekbar_blur").info['bounds']
        y = (bar['bottom'] + bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 100
        x = bar['left'] + inst * unit
        self.d.long_click(x, y)

    @teststep
    def select_backpic(self, inst=1):
        '''选择背景音乐'''
        self.d(resourceId="com.quvideo.xiaoying:id/btn_expand").click()
        self.d(resourceId="com.quvideo.xiaoying:id/collage_pic_item_cover", instance=inst - 1).click()

    @teststep
    def click_none_pic_btn(self):
        '''设定为默认背景'''
        self.d(resourceId="com.quvideo.xiaoying:id/pic_item_none").click()

    @teststep
    def click_other_pic_btn(self):
        '''点击其他相册'''
        self.d(resourceId="com.quvideo.xiaoying:id/collage_pic_item_other_album").click()

    @teststeps
    def select_folder(self, name='系统相册'):
        '''
        相册文件夹选择
        :param name: folder name textContains exp: '系统' will click folder'系统相册'
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/rc_folder", scrollable=True).fling.toBeginning()
        ele = self.d(resourceId="com.quvideo.xiaoying:id/rc_folder")
        rect = self.find_element_by_swipe_up(value=self.d(textContains=name), element=ele, steps=0.2).info['bounds']
        time.sleep(0.5)
        print(rect)
        x = (rect['right'] + rect['left']) / 2
        print(self.d.window_size())
        y = rect['top'] - self.d.window_size()[0] / 3
        print(x, y)
        self.d.long_click(x, y)

    @teststep
    def select_photo_clip(self, inst=1, preview=False):
        '''
        选择图片
        :param inst: inst=n 点击第n个clips
        :param preview: if True click gallery_preview_button
        :return:
        '''
        if not preview:
            self.d(resourceId="com.quvideo.xiaoying:id/img_click_mask", instance=inst - 1).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/img_click_mask", instance=inst - 1).sibling(
                className="android.widget.RelativeLayout").click()


class trim_cut_page(BasePage):
    '''修剪操作页面'''

    def click_trim_btn(self):
        '''点击修剪按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/trim_button").click()

    def click_cut_btn(self):
        '''点击剪中间按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/cut_button").click()

    def get_trim_time(self):
        '''获取trim时长'''
        trim_time = self.d(resourceId="com.quvideo.xiaoying:id/ve_split_right_time").get_text()
        return trim_time

    def trim_swipe(self):
        '''左右滑动trim及微调trim，只有初次进入才能操作成功（trimbar无法定位）'''
        print('original clip time is：%s 秒' % self.get_trim_time())
        trim = self.d(resourceId="com.quvideo.xiaoying:id/ve_gallery").info['bounds']
        unit = int(trim["right"] - trim["left"]) / 7
        y = int(trim["top"] + (trim["bottom"] - trim["top"]) / 2)
        self.d.swipe(int(trim["left"]) + unit / 4, y, int(trim["left"]) + 3 * unit, y, duration=0.1)
        print('after left_trim swipe clip time is：%s 秒' % self.get_trim_time())
        edit_page().preview_swipe_left()
        print(self.get_trim_time())
        self.d.swipe(int(trim["right"]) - unit / 4, y, int(trim["right"]) - 3 * unit, y, duration=0.1)
        print('after right_trim swipe time is：%s 秒' % self.get_trim_time())
        edit_page().preview_swipe_right()
        print(self.get_trim_time())


class split_page(BasePage):
    @teststeps
    def split_select(self, inst=30):
        '''
        设定分割的百分比位置
        :param inst:[0:100]
        :return: 截取点的时间 单位/s
        '''
        ele = self.d(resourceId="com.quvideo.xiaoying:id/ve_gallery").info['bounds']
        y = (ele['bottom'] + ele['top']) / 2
        unit = (ele['right'] - ele['left']) / 16
        x = unit + ele['left'] + inst * unit * 14 / 100
        self.d.long_click(x, y)
        total_time = split_page().get_total_time()
        split_time = total_time * inst / 100
        return split_time

    @teststep
    def get_total_time(self):
        '''获取clip时长'''
        total = self.d(resourceId="com.quvideo.xiaoying:id/ve_split_right_time").get_text().split(":")
        trim_time = float(total[0]) * 60 + float(total[1])
        return trim_time


if __name__ == '__main__':
    from Public.Log import Log
    from PageObject import gallery

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    # scale_page().click_fit_btn()
    # scale_page().select_scale("4:3")
    # scale_page().pinch_view("out")
    # scale_page().pinch_view("out")
    # scale_page().pinch_view()
    # scale_page().select_blur_alpha(99)
    # scale_page().select_colour()
    # scale_page().select_backpic(5)
    # trim_cut_page().trim_swipe()
    # print(edit_page().is_focused(3))
    # BasePage().d.app_install()
    # print(split_page().split_select(30))
    # BasePage().set_fastinput_ime()
    edit_page().effect_view_swipe_left()
