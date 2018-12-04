// pages/index/share.js
var app = getApp();
Page({

  /**
   * Page initial data
   */
  data: {
    num: 4,//后端给的分数,显示相应的星星
    one_1: '',
    two_1: '',
    one_2: 0,
    two_2: 5,
    eflag:false,
    star:false,
    emotion:"",
    pageBackgroundColor: '#BBBBBB',
    bool_display:'block',
    hiddenflag:true,
    items: [
      { name: 'SAD', value: '伤心' },
      { name: 'HAPPY', value: '开心'},
      { name: 'ANGRY', value: '急眼' },
      { name: 'MOVE', value: '感动哭了' },
    ]
  },
  radioChange: function (e) {
    console.log('radio发生change事件，携带value值为：', e.detail.value)
    this.setData({
      eflag:true,
      emotion: e.detail.value
    })
    if(this.data.star){
      this.setData({
        pageBackgroundColor: '#4DD52B',
      })
    }
  },
  submit_l:function(){
    var that = this
    this.setData({
      bool_display: 'none',
      hiddenflag:false,
    })
    if (this.data.star& this.data.eflag) {
      console.log(this.data.one_2)
      console.log(this.data.emotion)
      wx.request({
        url: "http://poeticimage.eastus.cloudapp.azure.com:8000/",
        method: "POST",
        data: {
          type:"comment",
          id:app.globalData.id,
          stars: that.data.one_2,
          emotions:that.data.emotion
        },
        header: {
          "Content-Type": "application/json"
        },
        success: function (res) {
          console.log("上传成功")
        },
      })
      wx.navigateTo({
        url: 'thanks'
      })
    }
  },

  /**
   * Lifecycle function--Called when page load
   */
  onLoad: function (options) {

  },

  /**
   * Lifecycle function--Called when page is initially rendered
   */
  onReady: function () {

  },
  in_xin: function (e) {  //in_xin是个变量，one_2是5，two_2是0
    var in_xin = e.currentTarget.dataset.in;
    var one_2;
    if (in_xin === 'use_sc2') {   //界面在星星上
      one_2 = Number(e.currentTarget.id);
    } else {
      one_2 = Number(e.currentTarget.id) + this.data.one_2;
    }
    this.setData({
      one_2: one_2,
      two_2: 5 - one_2,
      star:true
    })
    if (this.data.eflag) {
      this.setData({
        pageBackgroundColor: '#4DD52B',
      })
    }
  },
  /**
   * Lifecycle function--Called when page show
   */
  onShow: function () {

  },

  /**
   * Lifecycle function--Called when page hide
   */
  onHide: function () {

  },

  /**
   * Lifecycle function--Called when page unload
   */
  onUnload: function () {

  },

  /**
   * Page event handler function--Called when user drop down
   */
  onPullDownRefresh: function () {

  },

  /**
   * Called when page reach bottom
   */
  onReachBottom: function () {

  },

  /**
   * Called when user click on the top right corner to share
   */
  onShareAppMessage: function () {

  }
})

