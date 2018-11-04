#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.BasePage import BasePage
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError
from Public.Log import Log

log = Log()


class community_page(BasePage):
    '''社区首页,包含推荐页面操作'''

    @teststep
    def click_search_btn(self):
        '''点击搜索按钮'''
        log.i("点击搜索按钮")
        self.d(resourceId="com.quvideo.xiaoying:id/btn_search").click()

    @teststep
    def click_message_btn(self):
        log.i('点击消息按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_message").click()

    @teststep
    def select_Bar(self, inst=1):
        log.i('1-关注，2-推荐，3-发现，点击 %s' % inst)
        self.d(resourceId="android:id/text1", instance=inst - 1).click()

    @teststep
    def click_label(self, title):
        log.i('点击推荐页下的标签')
        self.d(resourceId="com.quvideo.xiaoying:id/recyclerViewCategory").child(text=title).click()

    @teststep
    def select_video_thumb(self, inst=1):
        log.i('点击推荐页内的第%s个视频' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/img_video_thumb", className="android.widget.ImageView",
               instance=inst - 1).click()

    @teststep
    def get_videolike_count(self, inst=1):
        log.i('获取推荐页面下第%s个视频的点赞数' % inst)
        like_count = self.d(resourceId="com.quvideo.xiaoying:id/thumb_layout",
                            className="android.widget.RelativeLayout",
                            instance=inst - 1).child(resourceId="com.quvideo.xiaoying:id/text_like_count").get_text()
        log.i('点赞数为 %s' % like_count)
        return like_count

    @teststep
    def select_fab_menu(self, inst=1):
        log.i('添加按钮，选择1-拍摄,2-相册,点击%s' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/fab_expand_menu_button").click()
        self.d(resourceId="com.quvideo.xiaoying:id/viva_float_btn_img", className="android.widget.ImageView",
               instance=inst - 1).click()

    @teststep
    def fab_menu_exists(self):
        log.i('检查添加按钮是否存在')
        return self.d(resourceId="com.quvideo.xiaoying:id/fab_expand_menu_button").exists


class video_list_page(BasePage):
    '''关注页面、个人详情视频列表页面'''

    @teststep
    def get_headinfo(self, inst=1):
        '''
        获取视频信息
        :param inst: viode的顺序 默认第一个 inst=1
        :return: nickname, public_time, play_count
        '''
        log.i('获取视频列表页面第%s个视频的信息' % inst)
        nickname = self.d(resourceId="com.quvideo.xiaoying:id/videocard_id", instance=inst - 1). \
            child(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_owner_nickname").get_text()
        public_time = self.d(resourceId="com.quvideo.xiaoying:id/videocard_id", instance=inst - 1). \
            child(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_public_time").get_text()
        play_count = self.d(resourceId="com.quvideo.xiaoying:id/videocard_id", instance=inst - 1). \
            child(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_play_count").get_text()
        if self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_video_card_title", instance=inst - 1).exists:
            videotitle = self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_video_card_title",
                                instance=inst - 1).get_text()
        else:
            videotitle = None
        # like_count = self.d(resourceId="com.quvideo.xiaoying:id/videocard_id", instance=inst - 1). \
        #     child(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_like_count").get_text()
        log.i('用户名：%s ；发布时间：%s ；播放数：%s ；视频标题：%s ' % (nickname, public_time, play_count, videotitle))
        return nickname, public_time, play_count, videotitle

    @teststep
    def click_nickname(self, name=None):
        log.i('点击用户名,跳转到用户详情页面')
        if name:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_owner_nickname", text=name).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_owner_nickname").click()

    @teststep
    def click_video_title(self, title=None):
        log.i('点击视频标题,跳转到视频详情页面')
        if title:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_video_card_title", text=title).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_video_card_title").click()

    @teststep
    def click_video_detail_head(self, inst=1):
        log.i('点击第%s个视频顶部，跳转到视频详情页面' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_video_detail_head_layout", instance=inst - 1).click()

    def swipe_to_video_bottom_layout(self):
        '''上滑到视频底部 直到出分享按钮'''
        self.find_element_by_swipe_up(self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_share_count"), steps=0.5)

    def click_like_btn(self):
        log.i('点击点赞按钮')
        self.swipe_to_video_bottom_layout()
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_layout_like").click()

    def get_like_count(self):
        log.i('获取点赞数')
        self.swipe_to_video_bottom_layout()
        if self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_layout_like").\
            child(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_like_count").exists:
            count = self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_layout_like").\
                child(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_like_count").get_text()
        else:
            count = 0
        log.i('点赞数：%s' % count)
        return int(count)

    def click_comment_btn(self):
        log.i('点击评论按钮')
        self.swipe_to_video_bottom_layout()
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_comment").click()

    def get_comment_count(self):
        log.i('获取评论数')
        self.swipe_to_video_bottom_layout()
        count = self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_comment").get_text()
        if count:
            pass
        else:
            count = 0
        log.i('评论数：%s' % count)
        return int(count)

    def video_download(self):
        log.i('点击下载按钮')
        self.swipe_to_video_bottom_layout()
        if self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_download").exists:
            self.watch_device('确认')
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_text_download").click()
            toast1 = self.d.toast.get_message(1, 4)
            log.i('toast is %s' % toast1)
            self.unwatch_device()
        else:
            log.i('视频不支持下载')

    def get_download_count(self):
        log.i('获取视频下载数')
        self.swipe_to_video_bottom_layout()
        if self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_download_count").exists:
            count = self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_download_count").get_text()
        else:
            count =0
        log.i('下载数：%s' % count)
        return int(count)







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
    def commet_lick_btn_click(self, inst=1):
        '''点击评论中的点赞'''
        self.d(resourceId="com.quvideo.xiaoying:id/commentLikeCount", instance=inst - 1).click()

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
        self.d(resourceId="com.quvideo.xiaoying:id/text_count", instance=inst - 1).click()

    @teststep
    def is_like_tab(self):
        '''
        是否在喜欢tab下
        :return: true false
        '''
        return self.d(resourceId="com.quvideo.xiaoying:id/text_count", instance=1). \
            sibling(resourceId="com.quvideo.xiaoying:id/img_cursor_line").wait(timeout=3)

    @teststep
    def click_back_top_btn(self):
        '''点击返回顶部按钮'''
        if self.d(resourceId="com.quvideo.xiaoying:id/creation_back_top").exists:
            self.d(resourceId="com.quvideo.xiaoying:id/creation_back_top").click()
            return True
        else:
            return False


class fans_follow_list_page(BasePage):
    '''粉丝列表\关注列表页面'''

    @teststep
    def click_avatar(self, inst=1):
        log.i('点击列表头像')
        self.d(resourceId="com.quvideo.xiaoying:id/avatar_img", instance=inst - 1).click()

    @teststeps
    def click_follow_btn(self, inst=1):
        log.i('关注/取消关注操作')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_follow_state", instance=inst - 1).click()
        self.d(resourceId="com.quvideo.xiaoying:id/buttonDefaultPositive").click_exists()

    @teststep
    def get_info(self, inst=1):
        '''获取列表用户信息'''
        name = self.d(resourceId="com.quvideo.xiaoying:id/fans_name", instance=inst - 1).get_text()
        if self.d(resourceId="com.quvideo.xiaoying:id/fans_desc", instance=inst - 1).exists:
            desc = self.d(resourceId="com.quvideo.xiaoying:id/fans_desc", instance=inst - 1).get_text()
        else:
            desc = None
        follow_state = self.d(resourceId="com.quvideo.xiaoying:id/btn_follow_state", instance=inst - 1).get_text()
        return name, desc, follow_state


class notify_page(BasePage):
    '''消息页面'''

    def select_tab(self, inst=1):
        '''
        点击消息也顶部tab 动态、消息
        :param inst: 1-动态  2-消息
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/text_viewpager_tab", instance=inst - 1).click()

    @teststep
    def get_imgicon_info(self, inst=1):
        '''
        获取消息下按钮名称及未读数
        :param inst: 按钮数
        :return: exp：('赞', 0)
        '''
        ele = self.d(resourceId="com.quvideo.xiaoying:id/imgIcon", instance=inst - 1)
        name = ele.sibling(className="android.widget.TextView")[1].get_text()
        count = ele.sibling(className="android.widget.TextView").get_text()
        try:
            count = int(ele.sibling(className="android.widget.TextView").get_text())
        except:
            return count, 0
        else:
            return name, count

    @teststep
    def click_imgicon_btn(self, inst=1):
        '''点击消息下的点赞、评论、@我、粉丝的图标按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/imgIcon", instance=inst - 1).click()

    @teststep
    def click_message_img_avatar(self, inst=1):
        '''点击消息列表中的头像'''
        self.d(resourceId="com.quvideo.xiaoying:id/message_img_avatar", instance=inst - 1).click()

    @teststep
    def click_message_video_thumb(self, inst=1):
        '''点击消息列表中的视频缩略图'''
        self.d(resourceId="com.quvideo.xiaoying:id/message_video_thumb", instance=inst - 1).click()

    @teststep
    def get_message_info(self, inst=1):
        '''
        获取消息列表信息，获取动态页面信息
        :return: name, sub, msg_time
        '''
        name = self.d(resourceId="com.quvideo.xiaoying:id/text_name", instance=inst - 1).get_text()
        if self.d(resourceId="com.quvideo.xiaoying:id/text_sub").exists:
            sub = self.d(resourceId="com.quvideo.xiaoying:id/text_sub", instance=inst - 1).get_text()
        else:
            sub = None
        msg_time = self.d(resourceId="com.quvideo.xiaoying:id/message_time", instance=inst - 1).get_text()
        return name, sub, msg_time

    @teststep
    def get_fans_message_info(self, inst=1):
        '''获取粉丝消息列表信息'''
        name = self.d(resourceId="com.quvideo.xiaoying:id/msg_fans_name", instance=inst - 1).get_text()
        msg_time = self.d(resourceId="com.quvideo.xiaoying:id/msg_fans_time", instance=inst - 1).get_text()
        return name, msg_time

    @teststep
    def click_fans_message_avatar(self, inst=1):
        '''点击粉丝消息头像'''
        self.d(resourceId="com.quvideo.xiaoying:id/msg_fans_avatar_img", instance=inst - 1).click()

    @teststep
    def click_fans_message_follow_btn(self, inst=1):
        '''点击粉丝消息关注按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/msg_follow_state", instance=inst - 1).click()

    # @teststep
    # def get_friends_info(self,inst=1):
    #     self.


class search_page(BasePage):
    '''搜索页面'''

    @teststeps
    def search_keyword(self, text):
        '''搜索页输入关键字搜索'''
        self.d(resourceId="com.quvideo.xiaoying:id/edittext_search").click()
        self.d.clear_text()
        self.d.send_keys(text)  # adb广播输入
        # self.d.clear_text()  # 清除输入框所有内容(Require android-uiautomator.apk version >= 1.0.7)
        self.d.send_action("search")
        time.sleep(2)

    @teststep
    def click_search_results_tab(self, inst=2):
        '''
        搜索后点击对于的搜索结果tab 默认点击 用户tab
        :param text: 1-综合、2-用户、3-话题、4-视频
        :return:
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/text_viewpager_tab", instance=inst - 1).click()

    @teststep
    def clear_search_text(self):
        '''点击搜索框的×'''
        self.d(resourceId="com.quvideo.xiaoying:id/edittext_search").click()
        self.d(resourceId="com.quvideo.xiaoying:id/btn_clear_edit").click()

    @teststeps
    def clear_search_history(self):
        self.d(text=u"我搜过的").sibling(className="android.widget.ImageView").click()
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive").click_exists()

    @teststep
    def click_cancel_btn(self):
        '''点击取消按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/btn_back").click()

    @teststep
    def get_search_history(self):
        '''
        获取我搜索过的关键字
        :return: list exp:['嘻嘻嘻', '哈哈哈']
        '''

        his_list = []
        count = int(self.d(resourceId="com.quvideo.xiaoying:id/tagSearchSetView").child(
            className="android.widget.TextView").count)
        for i in range(count):
            his_list.append(self.d(resourceId="com.quvideo.xiaoying:id/tagSearchSetView").
                            child(className="android.widget.TextView")[i].get_text())
        return his_list

    @teststep
    def get_hot_search(self):
        '''
        获取热门搜索的title
        :return: list exp：['朗读者行动', '笑掉大门牙', '神曲', '颜值担当', '舞分之一']
        '''
        hot_list = []
        count = int(self.d(resourceId="com.quvideo.xiaoying:id/recyclerView").child(
            className="android.widget.LinearLayout").count)
        for i in range(count):
            hot_list.append(self.d(resourceId="com.quvideo.xiaoying:id/recyclerView").child(
                className="android.widget.LinearLayout")[i].child(
                className="android.widget.TextView")[1].get_text())
        return hot_list

    @teststep
    def click_recommend_avatar(self, inst=1):
        '''
        点击推荐的头像并返回 推荐账号的c 名称及tag
        :param inst: 推荐的顺序 默认第一个
        :return:exp：('环球梦游记', '女神')
        '''
        name = self.d(resourceId="com.quvideo.xiaoying:id/textview_name", instance=inst - 1).get_text()
        tag = self.d(resourceId="com.quvideo.xiaoying:id/textview_tag1", instance=inst - 1).get_text()
        self.d(resourceId="com.quvideo.xiaoying:id/img_avatar", instance=inst - 1).click()
        return name, tag


if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    # BasePage().d.debug=True

    # search_page().search_keyword('哈哈哈')
    # search_page().search_keyword('嘻嘻嘻')
    # search_page().click_search_results_tab('视频')
    # inf=search_page().get_search_history()
    # print(inf)
    # BasePage().d(text=inf[0]).click()
    # search_page().clear_search_text()
    # fan_list_page().click_fan()
    # print(fan_list_page().get_fan_info())
    # video_list_page().get_headinfo()
    # video_list_page().click_nickname()
    # video_list_page().get_like_count()
    # video_list_page().click_like_btn()
    # video_list_page().get_like_count()
    # video_list_page().get_download_count()
    video_list_page().video_download()
    # BasePage().d.click(507.0, 1852.0)