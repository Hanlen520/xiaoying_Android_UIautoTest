#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.BasePage import BasePage
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class Recommend_Page(BasePage):
    '''推荐页'''

    @teststep
    def click_label(self, title):
        '''点击推荐页下的标签'''
        self.d(resourceId="com.quvideo.xiaoying:id/recyclerViewCategory").child(text=title).click()

    @teststep
    def click_video_thumb(self, inst=1):
        '''
        点击推荐页内的视频
        :param inst: 点击视频的顺序，ins=1 点击页面第一个视频
        :return: None
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/img_video_thumb", className="android.widget.ImageView",
               instance=inst - 1).click()

    @teststep
    def get_videolike_count(self, inst=1):
        like_count = self.d(resourceId="com.quvideo.xiaoying:id/thumb_layout",
                            className="android.widget.RelativeLayout",
                            instance=inst - 1).child(resourceId="com.quvideo.xiaoying:id/text_like_count").get_text()
        return like_count

    @teststep
    def click_fab_menu(self, inst=1):
        '''
        点击添加按钮，选择拍摄或打开相册
        :param inst: ins=1 拍摄； inst=2 相册
        :return:
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/fab_expand_menu_button").click()
        self.d(resourceId="com.quvideo.xiaoying:id/viva_float_btn_img", className="android.widget.ImageView",
               instance=inst - 1).click()

    @teststep
    def fab_menu_exists(self):
        '''
        检查添加按钮是否存在
        :return:
        '''
        return self.d(resourceId="com.quvideo.xiaoying:id/fab_expand_menu_button").exists


class Follow_Page(BasePage):
    '''关注页面'''

    def get_headinfo(self, inst=1):
        '''
        获取视频信息
        :param inst: viode的顺序 默认第一个 inst=1
        :return: nickname, public_time, play_count
        '''
        nickname = self.d(resourceId="com.quvideo.xiaoying:id/videocard_id", instance=inst - 1). \
            child(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_owner_nickname").get_text()
        public_time = self.d(resourceId="com.quvideo.xiaoying:id/videocard_id", instance=inst - 1). \
            child(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_public_time").get_text()
        play_count = self.d(resourceId="com.quvideo.xiaoying:id/videocard_id", instance=inst - 1). \
            child(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_play_count").get_text()
        videotitle = self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_video_card_title",
                            instance=inst - 1).get_text()
        # like_count = self.d(resourceId="com.quvideo.xiaoying:id/videocard_id", instance=inst - 1). \
        #     child(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_like_count").get_text()
        return nickname, public_time, play_count, videotitle

    def click_nickname(self, name=None):
        if name:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_owner_nickname", text=name).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_owner_nickname").click()

    def click_videotitle(self, title=None):
        if title:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_video_card_title", text=title).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_video_card_title").click()


class FeedVideo_Page(BasePage):
    '''沉浸Feed视频页面'''

    @teststep
    def get_video_info(self):
        '''获取当前feed视频的信息，title, description, playcount, likecount, commentcount, sharecount'''
        title = self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_title").get_text()
        playcount = self.d(resourceId="com.quvideo.xiaoying:id/feed_playcount_action").get_text()
        likecount = self.d(resourceId="com.quvideo.xiaoying:id/feed_like_action").get_text()
        commentcount = self.d(resourceId="com.quvideo.xiaoying:id/feed_comment_action").get_text()
        sharecount = self.d(resourceId="com.quvideo.xiaoying:id/feed_share_action").get_text()
        if self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_text").exists:
            description = self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_text").get_text()
        else:
            description = None
        return title, description, playcount, likecount, commentcount, sharecount

    @teststep
    def get_current_time(self):
        '''获取当前播放进度时长'''
        if self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_seek_current_time").exists:
            pass
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_seek_video_seekbar2").click()
        current_time = self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_seek_current_time").get_text()
        # total_time = self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_seek_total_time").get_text()
        return current_time

    @teststep
    def get_total_time(self):
        '''获取当前视频总时长'''
        if self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_seek_total_time").exists:
            pass
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_seek_video_seekbar2").click()
        total_time = self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_seek_total_time").get_text()
        return total_time

    @teststep
    def click_head_btn(self):
        '''点击头像图标'''
        self.d(resourceId="com.quvideo.xiaoying:id/feed_bottom_head").click()

    @teststep
    def click_follow_state(self):
        '''点击头像边上的关注按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/feed_bottom_head_follow_state").click_exists()

    @teststep
    def click_lick_btn(self):
        '''点击点赞按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/feed_like_action").click_exists()

    @teststep
    def click_comment_btn(self):
        '''点击评论按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/feed_comment_action").click()

    @teststep
    def get_comment_info(self, inst=1):
        if self.d(resourceId="com.quvideo.xiaoying:id/layout_content").exists:
            name = self.d(resourceId="com.quvideo.xiaoying:id/layout_content", instance=inst - 1). \
                child(resourceId="com.quvideo.xiaoying:id/textview_name").get_text()
            time = self.d(resourceId="com.quvideo.xiaoying:id/layout_content", instance=inst - 1). \
                child(resourceId="com.quvideo.xiaoying:id/textview_publish_time").get_text()
            content = self.d(resourceId="com.quvideo.xiaoying:id/layout_content", instance=inst - 1). \
                child(resourceId="com.quvideo.xiaoying:id/textview_content").get_text()
            LikeCount = self.d(resourceId="com.quvideo.xiaoying:id/layout_content", instance=inst - 1). \
                child(resourceId="com.quvideo.xiaoying:id/commentLikeCount").get_text()
            return content, name, time, LikeCount
        else:
            return Exception('No Comment yet')

    @teststep
    def comment_reply(self, inst=1):
        '''点击评论 回复评论'''
        self.d(resourceId="com.quvideo.xiaoying:id/layout_content", instance=inst - 1).click()
        text = self.d(resourceId="com.quvideo.xiaoying:id/edit_text_comment").get_text()
        print('点击评论后 输入框显示文字为：\n %s' % text)
        self.d(resourceId="com.quvideo.xiaoying:id/edit_text_comment").set_text("哈哈哈")
        self.d(resourceId="com.quvideo.xiaoying:id/btn_send").click()

    def comment_add(self):
        '''添加评论'''
        self.d(resourceId="com.quvideo.xiaoying:id/edit_text_comment").set_text("哈哈哈")
        self.d(resourceId="com.quvideo.xiaoying:id/btn_send").click()

    @teststep
    def click_share_btn(self):
        '''点击分享按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/feed_share_action").click()

    @teststep
    def click_more_btn(self):
        '''点击更多按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/feed_more_action").click()

    @teststep
    def click_RamaDanMode_btn(self, status=1):
        '''
        点击斋月模式按钮
        :param status: status=1 开启斋月模式  else 关闭斋月模式
        :return: None
        '''
        if status == 1:
            self.d(resourceId="com.quvideo.xiaoying:id/btnRamaDanMode").click()
            if self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive").exists:
                self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive").click()
            else:
                self.d(resourceId="com.quvideo.xiaoying:id/btnRamaDanMode").click_exists()
                self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive").click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/btnRamaDanMode").click()
            if self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive").exists:
                self.back()
            else:
                pass

    @teststep
    def click_MuteMode_btn(self):
        '''点击静音按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/btnMuteMode").click()


class UserInfo_Page(BasePage):
    '''用户详情 页面'''
    @teststep
    def get_user_info(self):
        '''
        获取用户信息
        :return: name, introduce, id, zan_count, fans_count, follow_count, works_count, likes_count
        '''
        name = self.d(resourceId="com.quvideo.xiaoying:id/user_other_title_text").get_text()
        introduce = self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_studio_account_introduce").get_text()
        id = self.d(resourceId="com.quvideo.xiaoying:id/user_other_title_id").get_text()
        zan_count = self.d(resourceId="com.quvideo.xiaoying:id/user_zan_count").get_text()
        fans_count = self.d(resourceId="com.quvideo.xiaoying:id/user_fans_count").get_text()
        follow_count = self.d(resourceId="com.quvideo.xiaoying:id/user_follow_count").get_text()
        works_count = str(self.d(resourceId="com.quvideo.xiaoying:id/studio_view_pager_tab_view").\
            child(resourceId="com.quvideo.xiaoying:id/text_count",instance=0).get_text()).split(" ")[1]
        likes_count = str(self.d(resourceId="com.quvideo.xiaoying:id/studio_view_pager_tab_view").\
            child(resourceId="com.quvideo.xiaoying:id/text_count",instance=1).get_text()).split(" ")[1]
        return name, introduce, id, zan_count, fans_count, follow_count, works_count, likes_count

    @teststep
    def click_avatar_img(self):
        '''点击头像'''
        self.d(resourceId="com.quvideo.xiaoying:id/img_avatar").click()

    @teststep
    def click_zannum_btn(self):
        '''
        点击获赞数按钮，并自动关闭dialog
        :return: dialog内容
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/user_zan_layout").click()
        content = self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_alert_dialog_content").get_text()
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive").click()
        return content

    @teststep
    def click_fansnum_btn(self):
        '''点击粉丝数'''
        self.d(resourceId="com.quvideo.xiaoying:id/user_fans_layout").click()

    @teststep
    def click_follownum_btn(self):
        '''点击关注数'''
        self.d(resourceId="com.quvideo.xiaoying:id/user_follow_layout").click()

    @teststep
    def click_follow_btn(self):
        '''点击关注'''
        return self.d(resourceId="com.quvideo.xiaoying:id/user_follow_btn").click_exists()

    @teststep
    def click_chat_btn(self):
        '''点击私信'''
        return self.d(resourceId="com.quvideo.xiaoying:id/user_chat_btn").click_exists()




if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver('10.0.29.65')
    # print(FeedVideo_Page().get_comment_info())
    # FeedVideo_Page().comment_add()

    print(UserInfo_Page().get_user_info())
    UserInfo_Page().click_avatar_img()
    BasePage().back()
    print(UserInfo_Page().click_zannum_btn())
    UserInfo_Page().click_fansnum_btn()
    BasePage().back()
    UserInfo_Page().click_follownum_btn()
    BasePage().back()
    print(UserInfo_Page().click_follow_btn())
    print(UserInfo_Page().click_chat_btn())


