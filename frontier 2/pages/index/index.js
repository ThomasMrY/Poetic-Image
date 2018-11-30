var app = getApp();

Page({
  clickMe: function (){
      wx.navigateTo({
        url: 'next'
      })
  },
  
  data: {
    items: [
      { value: '1', name: '枯藤老树昏鸦，小桥流水人家' },
      { value: '2', name: '窗前明月光，疑是地上霜'  },
      { value: '3', name: '举头望明月，低头思故乡' }
    ]
  },
  radioChange(e) {
    console.log('用户选择了', e.detail.value)

    const items = this.data.items
    for (let i = 0, len = items.length; i < len; ++i) {
      items[i].checked = items[i].value === e.detail.value
    }

    this.setData({
      items
    })
  },
    onLoad: function () {
        var _this = this;
        console.log(app.globalData.ImgSrc)
        if (app.globalData.userInfo) {
            this.setData({
                images: [app.globalData.ImgSrc],
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
});