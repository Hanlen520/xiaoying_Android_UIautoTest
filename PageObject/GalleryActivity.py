#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.BasePage import BasePage
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class Gallery_Page(BasePage):
    '''gallery页面'''

    @teststep
    def choose_gallery(self, select=0):
        '''
        点击切换视频 、图片
        :param select: 1-->video  2-->photo 0&other--> pass
        :return:gallery_title
        '''

        if select == 1:
            self.d(resourceId="com.quvideo.xiaoying:id/gallery_chooser_layout").click()
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_gallery_video_tab").click()
        elif select == 2:
            self.d(resourceId="com.quvideo.xiaoying:id/gallery_chooser_layout").click()
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_gallery_photo_tab").click()
        else:
            pass
        gallery_title = self.d(resourceId="com.quvideo.xiaoying:id/gallery_title").get_text()
        return gallery_title

    @teststep
    def choose_gallery_tab(self, tab=1):
        '''
        全部、其他相册点击切换
        :param tab: 1-->全部  2-->其他相册
        :return:
        '''
        if tab == 1:
            self.d(text='全部').click()
        elif tab == 2:
            self.d(text=u"其他相册").click()

    @teststep
    def click_folder(self, name='系统相册'):
        '''
        其他相册，点击文件夹
        :param name: folder name textContains exp: '系统' will click folder'系统相册'
        '''
        ele = self.d(resourceId="com.quvideo.xiaoying:id/gallery_viewpager")
        rect = self.find_element_by_swipe_up(value=self.d(textContains=name), element=ele).info['bounds']
        time.sleep(0.5)
        x = (rect['right'] + rect['left']) / 2
        y = rect['bottom'] - self.d.window_size()[0] / 2.2
        self.d.click(x, y)

    @teststep
    def click_video_clip(self, inst=1):
        '''
        clip选择，点击视频缩略图
        :param instance: inst=n 点击第n个clips
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/img_icon", instance=inst - 1).click()

    @teststep
    def click_photo_clip(self, inst=1, preview=False):
        '''

        :param inst: inst=n 点击第n个clips
        :param preview: if True click gallery_preview_button
        :return:
        '''
        if not preview:
            self.d(resourceId="com.quvideo.xiaoying:id/img_click_mask", instance=inst - 1).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/img_click_mask", instance=inst - 1).sibling(
                className="android.widget.RelativeLayout").click()

    @teststep
    def click_up_down(self):
        '''
        点击升起、收回clips_board的按钮
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/layout_body").click()

    @teststep
    def delete_clip(self, inst=1):
        '''
        删除clipsboard上添加的clip
        :param inst: inst=n 删除第n个clip
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/img_delete", instance=inst - 1).click()

    @teststep
    def drag_clip(self, start=2, end=1):
        '''
        拖动clipboard上clip的顺序
        :param start: 被移动clips的顺序
        :param end:  移动到clips的位置
        :return:
        '''
        start_center = self.d(resourceId="com.quvideo.xiaoying:id/icon", instance=start - 1)
        end_center = self.d(resourceId="com.quvideo.xiaoying:id/icon", instance=end - 1).center()
        start_center.drag_to(end_center[0], end_center[1])

    @teststep
    def click_next_btn(self):
        '''点击下一步跳转到编辑页面'''
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_storyboard_next_btn").click()

    @teststep
    def click_close_btn(self):
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_btn_left").click()

    @teststep
    def leave_select(self, leave=True):
        if leave:
            self.d(resourceId="com.quvideo.xiaoying:id/buttonDefaultPositive").click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/buttonDefaultNegative").click()


class VideoTrim_Page(BasePage):
    '''视频剪取页面'''

    @teststep
    def get_trim_time(self):
        t = self.d(resourceId="com.quvideo.xiaoying:id/txtview_trimed_duration").get_text()
        return t

    @teststep
    def trim_swipe(self):
        '''
        进入剪取页面，左右滑动trim及微调trim，只有初次进入才能操作成功（trimbar无法定位）
        '''

        # 左边Trim 右移
        print('original clip time is：%s 秒' % self.get_trim_time())
        t_left = self.d(resourceId="com.quvideo.xiaoying:id/imgview_thumbnail").info['bounds']
        self.d.swipe(int(t_left['left']), t_left['top'], t_left['right'], t_left['top'], duration=0.3)
        time.sleep(1)
        print('after left_trim swipe clip time is： %s 秒' % self.get_trim_time())

        # 右边Trim 左移
        t_right = self.d(resourceId="com.quvideo.xiaoying:id/imgview_thumbnail", instance=4).info['bounds']
        self.d.swipe(int(t_right['right']), t_right['top'], t_right['left'], t_right['top'], duration=0.3)
        time.sleep(1)
        print('after right_trim swipe time is： %s 秒' % self.get_trim_time())

        # 左边trim 左滑preview微调
        preview = self.d(resourceId="com.quvideo.xiaoying:id/previewview").info['bounds']
        self.d.tap(t_left['right'], t_left['top'])
        time.sleep(2)  # preview 没加载出来，滑动无效，加个等待
        self.d.swipe(preview['right'] / 2, preview['bottom'] - 50, preview['left'], preview['bottom'] - 50)
        print('left slightly swipe time is： %s 秒' % self.get_trim_time())

        # 右边Trim 右滑preview微调
        self.d.tap(t_right['left'], t_left['top'])
        time.sleep(2)  # preview 没加载出来，滑动无效，加个等待
        self.d.swipe(preview['right'] / 2, preview['bottom'] - 50, preview['right'], preview['bottom'] - 50)
        print('right slightly swipe time is： %s 秒' % self.get_trim_time())

    @teststep
    def click_ratate_btn(self):
        self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_ratate").click()

    @teststep
    def click_crop_btn(self):
        self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_crop").click()

    @teststep
    def click_start_trim_btn(self):
        self.d(resourceId="com.quvideo.xiaoying:id/btn_start_trim").click()

    @teststep
    def click_import_btn(self):
        btn = self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_import")
        print('添加按钮文字：%s' % btn.get_text())
        btn.click()

    @teststep
    def click_play_btn(self):
        self.d(resourceId="com.quvideo.xiaoying:id/previewview").click()
        time.sleep(2)

    @teststep
    def click_close_btn(self):
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_btn_left").click()

    @teststep
    def leave_select(self, leave=True):
        if leave:
            self.d(resourceId="com.quvideo.xiaoying:id/buttonDefaultPositive").click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/buttonDefaultNegative").click()


if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    # BasePage().set_driver('10.0.28.14')
    BasePage().set_driver('10.0.28.164')
    p = VideoTrim_Page()
    # p.set_driver('10.0.28.164')
    # # p.gallery_choose(2)
    # p.click_folder('Mac')
    # p.click_clip(instance=3)
    # p.click_photo_clip(2)

    # p.delete_clip(3)
    # p.drag_clip(1, 4)
    # Gallery_Page().click_video_clip(1)
    # p.trim_swipe()
    # p.click_ratate_btn()
    # p.click_crop_btn()
    # p.click_start_trim_btn()
    # time.sleep(1)
    # p.click_start_trim_btn()
    # p.click_play_btn()
    #
    # p.click_close_btn()
    # p.leave_select(False)
    # p.click_import_btn()
    # p.click_play_btn()
    print(Gallery_Page().choose_gallery(2))
    # Gallery_Page().leave_select()
