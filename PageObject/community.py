#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.BasePage import BasePage
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class community_page(BasePage):
    '''社区首页,包含推荐页面操作'''

    @teststep
    def click_search_btn(self):
        '''点击搜索按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/btn_search").click()

    @teststep
    def click_message_btn(self):
        '''点击消息按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/btn_message").click()

    @teststep
    def select_Bar(self, inst=1):
        '''
        点击ActionBar上的 关注、推荐、发现
        :param inst: 1-关注，2-推荐，3-发现
        :return:
        '''
        self.d(resourceId="android:id/text1", instance=inst - 1).click()

    @teststep
    def click_label(self, title):
        '''点击推荐页下的标签'''
        self.d(resourceId="com.quvideo.xiaoying:id/recyclerViewCategory").child(text=title).click()

    @teststep
    def select_video_thumb(self, inst=1):
        '''
        点击推荐页内的视频
        :param inst: 点击视频的顺序，ins=1 点击页面第一个视频
        :return: None
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/img_video_thumb", className="android.widget.ImageView",
               instance=inst - 1).click()

    @teststep
    def get_videolike_count(self, inst=1):
        '''
        获取推荐页面下单个视频的点赞数
        :param inst: 视频的顺序，inst=1 默认第一个
        :return: like_count
        '''
        like_count = self.d(resourceId="com.quvideo.xiaoying:id/thumb_layout",
                            className="android.widget.RelativeLayout",
                            instance=inst - 1).child(resourceId="com.quvideo.xiaoying:id/text_like_count").get_text()
        return like_count

    @teststep
    def select_fab_menu(self, inst=1):
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


class follow_page(BasePage):
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
        '''点击用户名'''
        if name:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_owner_nickname", text=name).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_owner_nickname").click()

    def click_videotitle(self, title=None):
        '''点击视频标题'''
        if title:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_video_card_title", text=title).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_video_card_title").click()


class feedVideo_page(BasePage):
    '''沉浸Feed视频页面'''

    @teststep
    def get_video_info(self, name="title"):
        '''
        获取当前feed视频的信息 标题、播放量、点赞量、评论数、分享数、描述、下载数
        :param name: title play like comment share description download
        :return:
        '''
        if name == "title":
            if self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_title").exists:
                return self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_title").get_text()
            else:
                return Exception('No title')
        elif name == "play":
            if self.d(resourceId="com.quvideo.xiaoying:id/feed_playcount_action").exists:
                return self.d(resourceId="com.quvideo.xiaoying:id/feed_playcount_action").get_text()
            else:
                return Exception('No playcount')
        elif name == "like":
            if self.d(resourceId="com.quvideo.xiaoying:id/feed_like_action").exists:
                return self.d(resourceId="com.quvideo.xiaoying:id/feed_like_action").get_text()
            else:
                return Exception('No like count')
        elif name == "comment":
            if self.d(resourceId="com.quvideo.xiaoying:id/feed_comment_action").exists:
                return self.d(resourceId="com.quvideo.xiaoying:id/feed_comment_action").get_text()
            else:
                return Exception('No Comment')
        elif name == "share":
            if self.d(resourceId="com.quvideo.xiaoying:id/feed_share_action").exists:
                return self.d(resourceId="com.quvideo.xiaoying:id/feed_share_action").get_text()
            else:
                return Exception('No share count')
        elif name == "description":
            if self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_text").exists:
                return self.d(resourceId="com.quvideo.xiaoying:id/feed_desc_text").get_text()
            else:
                return Exception('No description')
        elif name == "download":
            if self.d(resourceId="com.quvideo.xiaoying:id/feed_download_action").exists:

                return self.d(resourceId="com.quvideo.xiaoying:id/feed_download_action").get_text()
            else:
                return Exception('No download count')


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
        '''
        获取评论信息
        :param inst: 评论顺序  默认第一个
        :return: content, name, time, LikeCount
        '''
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
    def click_at_btn(self):
        '''点击评论输入框的@按钮'''
        self.d(text=u"@", className="android.widget.TextView").click()

    @teststep
    def commet_lick_btn_click(self,inst =1):
        '''点击评论中的点赞'''
        self.d(resourceId="com.quvideo.xiaoying:id/commentLikeCount",instance=inst-1).click()
    @teststep
    def comment_reply(self, inst=1):
        '''点击评论 回复评论'''
        self.d(resourceId="com.quvideo.xiaoying:id/layout_content", instance=inst - 1).click()
        text = self.d(resourceId="com.quvideo.xiaoying:id/edit_text_comment").get_text()
        print('点击评论后 输入框显示文字为：\n %s' % text)
        self.d(resourceId="com.quvideo.xiaoying:id/edit_text_comment").set_text("哈哈哈")
        self.set_original_ime()
        self.d(resourceId="com.quvideo.xiaoying:id/btn_send").click()
        self.set_fastinput_ime()

    def comment_add(self):
        '''添加评论'''
        self.d(resourceId="com.quvideo.xiaoying:id/edit_text_comment").set_text("哈哈哈")
        self.set_original_ime()
        self.d(resourceId="com.quvideo.xiaoying:id/btn_send").click()
        self.set_fastinput_ime()

    @teststep
    def click_share_btn(self):
        '''点击分享按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/feed_share_action").click()

    @teststep
    def click_more_btn(self):
        '''点击更多按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/feed_more_action").click()

    @teststep
    def select_RamaDanMode(self, status=1):
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


class userinfo_page(BasePage):
    '''用户详情 页面,包含他人主页 我的主页'''

    @teststep
    def get_user_info(self, name="title"):
        '''
        获取用户信息 昵称 、id、简介、获赞数、粉丝数、关注数、作品数、喜欢数目
        :param name: title, id, introduce, zan, fans, follow, work, like
        :return:
        '''

        if name == "title":
            if self.d(resourceId="com.quvideo.xiaoying:id/studio_title_text").exists:
                return self.d(resourceId="com.quvideo.xiaoying:id/studio_title_text").get_text()
            else:
                return self.d(resourceId="com.quvideo.xiaoying:id/user_other_title_text").get_text()
        elif name == "id":
            if self.d(resourceId="com.quvideo.xiaoying:id/user_other_title_id").exists:
                return self.d(resourceId="com.quvideo.xiaoying:id/user_other_title_id").get_text()
            else:
                return self.d(resourceId="com.quvideo.xiaoying:id/studio_title_id").get_text()
        elif name == "introduce":
            return self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_studio_account_introduce").get_text()
        elif name == "zan":
            return self.d(resourceId="com.quvideo.xiaoying:id/user_zan_count").get_text()
        elif name == "fans":
            return self.d(resourceId="com.quvideo.xiaoying:id/user_fans_count").get_text()
        elif name == "follow":
            return self.d(resourceId="com.quvideo.xiaoying:id/user_follow_count").get_text()
        elif name == "work":
            return str(self.d(resourceId="com.quvideo.xiaoying:id/studio_view_pager_tab_view"). \
                          child(resourceId="com.quvideo.xiaoying:id/text_count", instance=0).get_text()).split(" ")[1]
        elif name == "like":
            return str(self.d(resourceId="com.quvideo.xiaoying:id/studio_view_pager_tab_view"). \
                          child(resourceId="com.quvideo.xiaoying:id/text_count", instance=1).get_text()).split(" ")[1]



    @teststep
    def click_share_btn(self):
        '''点击分享按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/btn_share").click()

    @teststep
    def select_more_action(self, text):
        '''
        点更多按钮，并选择相应功能
        :param text: 私信、复制 ID、举报该用户、直接拉黑
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/btn_more").click()
        self.d(resourceId="com.quvideo.xiaoying:id/title", text=text).click()

    @teststep
    def click_setting_btn(self):
        '''点击设置按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/btn_setting").click()

    @teststep
    def click_avatar_img(self):
        '''点击头像'''
        self.d(resourceId="com.quvideo.xiaoying:id/img_avatar").click()

    @teststeps
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

    @teststep
    def click_edit_info_bt(self):
        '''点击编辑资料'''
        self.d(resourceId="com.quvideo.xiaoying:id/user_edit_info").click()

    @teststep
    def select_tab(self, inst=1):
        '''
        选择作品或者喜欢
        :param inst: 1作品  2喜欢
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/text_count", instance=inst-1).click()


    @teststep
    def is_like_tab(self):
        '''
        是否在喜欢tab下
        :return: true false
        '''
        return self.d(resourceId="com.quvideo.xiaoying:id/text_count", instance=1).\
            sibling(resourceId="com.quvideo.xiaoying:id/img_cursor_line").wait(timeout=3)


    @teststep
    def click_back_top_btn(self):
        '''点击返回顶部按钮'''
        if self.d(resourceId="com.quvideo.xiaoying:id/creation_back_top").exists:
            self.d(resourceId="com.quvideo.xiaoying:id/creation_back_top").click()
            return True
        else:
            return False
if __name__ == '__main__':
    from Public.Log import Log
    Log().set_logger('udid', './log.log')
    BasePage().set_driver('10.0.29.65')
    # Community_Page().select_Bar(2)
    # print(UserInfo_Page().select_tab(2))
    # # print(UserInfo_Page().get_user_info())
    # print(UserInfo_Page().is_like_tab())
    # print(UserInfo_Page().is_like_tab())
    # print(FeedVideo_Page().get_video_info("title"))
    #     # print(FeedVideo_Page().get_video_info("description"))
    #     # print(FeedVideo_Page().get_video_info("play"))
    #     #
    #     # print(FeedVideo_Page().get_video_info("like"))
    #     # print(FeedVideo_Page().get_video_info("comment"))
    #     #
    #     # print(FeedVideo_Page().get_video_info("download"))
    #     # print(FeedVideo_Page().get_video_info("share"))
    #     # print(FeedVideo_Page().get_current_time())

    # print(UserInfo_Page().get_user_info("title"))
    # print(UserInfo_Page().get_user_info("id"))
    # print(UserInfo_Page().get_user_info("zan"))
    # print(UserInfo_Page().get_user_info("fans"))
    # print(UserInfo_Page().get_user_info("follow"))
    # print(UserInfo_Page().get_user_info("work"))
    # print(UserInfo_Page().get_user_info("like"))
    for i in range(5):
        BasePage().swipe_up(steps=0.05)
    print(userinfo_page().click_back_top_btn())




