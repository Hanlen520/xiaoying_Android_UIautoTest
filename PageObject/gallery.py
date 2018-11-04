#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.BasePage import BasePage
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError
from Public.Log import Log
log = Log()

class gallery_page(BasePage):
    '''gallery页面'''

    @teststep
    def select_gallery(self, select=0):
        '''
        点击切换视频 、图片
        :param select: 1-->video  2-->photo 0&other--> pass
        :return:gallery_title
        '''
        log.i('gallery视频 、图片切换')
        if select == 1:
            self.d(resourceId="com.quvideo.xiaoying:id/gallery_chooser_layout").click()
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_gallery_video_tab").click()
            log.i('切换到视频')
        elif select == 2:
            self.d(resourceId="com.quvideo.xiaoying:id/gallery_chooser_layout").click()
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_gallery_photo_tab").click()
            log('切换到图片')
        else:
            pass
        gallery_title = self.d(resourceId="com.quvideo.xiaoying:id/gallery_title").get_text()
        log.i('当前gallery在 %s 选择页面' % gallery_title)
        return gallery_title

    @teststep
    def select_gallery_tab(self, tab=1):
        '''
        全部、其他相册点击切换
        :param tab: 1-->全部  2-->其他相册
        :return:
        '''
        if tab == 1:
            log.i('切换到全部')
            self.d(text='全部').click()
        elif tab == 2:
            log.i('切换到其他相册')
            self.d(text=u"其他相册").click()

    @teststep
    def click_folder(self, name='系统相册'):
        '''
        其他相册，点击文件夹
        :param name: folder name textContains exp: '系统' will click folder'系统相册'
        '''
        log.i('其他相册，找到 %s 文件夹 并点击进入'% name)
        self.d(resourceId="com.quvideo.xiaoying:id/gallery_viewpager", scrollable=True).fling.toBeginning()
        ele = self.d(resourceId="com.quvideo.xiaoying:id/gallery_viewpager")
        rect = self.find_element_by_swipe_up(value=self.d(textContains=name), element=ele, steps=0.2).info['bounds']
        time.sleep(0.5)
        # print(rect)
        x = (rect['right'] + rect['left']) / 2
        # print(self.d.window_size())
        y = rect['top'] - self.d.window_size()[0]/3
        # print(x, y)
        self.d.long_click(x, y)

    # @teststep
    # def click_fo(self,text =):
    #     '''点击文件夹'''
    #     # self.d(resourceId="com.quvideo.xiaoying:id/gallery_viewpager", scrollable=True).fling.toBeginning()
    #     # self.d(resourceId="com.quvideo.xiaoying:id/rc_folder", scrollable=True).fling.toBeginning()
    #     self.d(resourceId="com.quvideo.xiaoying:id/gallery_viewpager", scrollable=True).scroll.to(text="微信")

    @teststep
    def select_video_clip(self, inst=1):
        '''
        clip选择，点击视频缩略图
        :param instance: inst=n 点击第n个clips
        '''
        log.i('视频clips选择，点击第%s 个clip'% inst)
        self.d(resourceId="com.quvideo.xiaoying:id/img_icon", instance=inst - 1).click()

    @teststep
    def select_photo_clip(self, inst=1, preview=False):
        '''
        选择图片
        :param inst: inst=n 点击第n个clips
        :param preview: if True click gallery_preview_button
        :return:
        '''
        log.i('图片clips选择 点击第%s个clip 进入预览=%s' % (inst, preview))
        if not preview:
            self.d(resourceId="com.quvideo.xiaoying:id/img_click_mask", instance=inst - 1).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/img_click_mask", instance=inst - 1).sibling(
                className="android.widget.RelativeLayout").click()

    @teststep
    def click_up_down(self):
        log.i('clipboard升起、收回的按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/layout_body").click()

    @teststep
    def delete_clip(self, inst=1):
        log.i('删除clipboard上第%s个clip')
        self.d(resourceId="com.quvideo.xiaoying:id/img_delete", instance=inst - 1).click()

    @teststep
    def drag_clip(self, start=2, end=1):
        log.i('拖动第%s个clip到第%s个clip的位置' % (start, end))

        start_clip = self.d(resourceId="com.quvideo.xiaoying:id/icon", instance=start - 1)
        # start.click()
        end_clip = self.d(resourceId="com.quvideo.xiaoying:id/icon", instance=end - 1).info["bounds"]
        if start > end:
            start_clip.drag_to(end_clip["left"], end_clip["top"])
        else:
            start_clip.drag_to(end_clip["right"], end_clip["bottom"])

        # start_center = self.d(resourceId="com.quvideo.xiaoying:id/icon", instance=start - 1)
        # end_center = self.d(resourceId="com.quvideo.xiaoying:id/icon", instance=end - 1).center()
        # start_center.drag_to(end_center[0], end_center[1])

    @teststep
    def click_next_btn(self):
        log.i('点击下一步跳转到编辑页面')
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_storyboard_next_btn").click()

    @teststep
    def click_close_btn(self):
        log.i('点击×按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_btn_left").click()

    @teststep
    def leave_select(self, leave=True):
        '''是否保存草稿弹窗选择，leave=True 保存'''
        log.i('保存草稿弹窗，点击保存=%s ' % leave)
        if leave:
            self.d(resourceId="com.quvideo.xiaoying:id/buttonDefaultPositive").click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/buttonDefaultNegative").click()


class videotrim_page(BasePage):
    '''视频剪取页面'''

    @teststep
    def get_trim_time(self):
        log.i('获取trim 时长')
        t = self.d(resourceId="com.quvideo.xiaoying:id/txtview_trimed_duration").get_text()
        log.i('时长为 %s'% t)
        return t

    @teststeps
    def trim_swipe(self):
        '''
        进入剪取页面，左右滑动trim及微调trim，只有初次进入才能操作成功（trimbar无法定位）
        '''
        log.i('剪取页面，左右滑动trim及微调trim操作')
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
        log.i('点击旋转按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_ratate").click()

    @teststep
    def click_crop_btn(self):
        log.i('点击crop缩放按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_crop").click()

    @teststep
    def click_start_trim_btn(self):
        log.i('点击剪刀按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_start_trim").click()

    @teststep
    def click_import_btn(self):
        log('点击添加按钮')
        btn = self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_import")
        print('添加按钮文字：%s' % btn.get_text())
        btn.click()

    @teststep
    def click_play_btn(self):
        log('播放按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/previewview").click()
        time.sleep(2)

    @teststep
    def click_close_btn(self):
        log.i('点击关闭按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_btn_left").click()

    @teststep
    def leave_select(self, leave=True):
        log.i('放弃操作弹窗选择 确认放弃=%s'% leave)
        if leave:
            self.d(resourceId="com.quvideo.xiaoying:id/buttonDefaultPositive").click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/buttonDefaultNegative").click()


if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    gallery_page().select_photo_clip(2)

    gallery_page().select_photo_clip(1,True)