$(function () {
    $('form').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            title: {
                validators: {
                    notEmpty: {
                        message: '标题不能为空'
                    },
                }
            },
        }
    });
});

$(function(){
    //获取要定位元素距离浏览器顶部的距离
    var navH = $(".w-e-toolbar").offset().top;
    //滚动条事件
    $(window).scroll(function(){
    //获取滚动条的滑动距离
      var scroH = $(this).scrollTop();
      //滚动条的滑动距离大于等于定位元素距离浏览器顶部的距离，就固定，反之就不固定
      if(scroH>=navH/2){
        $(".w-e-toolbar").css({"position":"fixed","width":"70%", "top":53,});
        $(".w-e-menu").click(function () {
            $(".w-e-panel-container").css({"position":"fixed","top": 80});
        });

      }else if(scroH<2*navH){
        $(".w-e-toolbar").css({"position":"static", "width":"100%"});
        $(".w-e-menu").click(function () {
            $(".w-e-panel-container").css({"position":"absolute", "top": 0});
        });
        $(".w-e-panel-container").css({"position":"absolute", "top": 0});
      }
    });
});