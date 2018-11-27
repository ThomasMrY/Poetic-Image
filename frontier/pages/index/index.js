"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var app = getApp();
Page({
  clickMe: function () {
    wx.navigateTo({
      url: 'next'
    })
  },
  onShow: function () {
    console.log(this.route)
  },
  data: {
    items: [
      { name: '1', value: '枯藤老树昏鸦，小桥流水人家' },
      { name: '2', value: '床前明月光，疑是地上霜' },
      { name: '3', value: '举头望明月，低头思故乡' }
    ]
  },
  checkboxChange: function (e) {
    console.log('checkbox发生change事件，携带value值为：', e.detail.value)
  },
    onLoad: function () {
        var _this = this;
        if (app.globalData.userInfo) {
            this.setData({
                userInfo: app.globalData.userInfo,
                hasUserInfo: true,
            });
        }
        else if (this.data.canIUse) {
            app.userInfoReadyCallback = function (res) {
                _this.setData({
                    userInfo: res,
                    hasUserInfo: true
                });
            };
        }
        else {
            wx.getUserInfo({
                success: function (res) {
                    app.globalData.userInfo = res.userInfo;
                    _this.setData({
                        userInfo: res.userInfo,
                        hasUserInfo: true
                    });
                }
            });
        }
    },
    getUserInfo: function (e) {
        console.log(e);
        app.globalData.userInfo = e.detail.userInfo;
        this.setData({
            userInfo: e.detail.userInfo,
            hasUserInfo: true
        });
    }
});