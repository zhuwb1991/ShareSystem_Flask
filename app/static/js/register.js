$(function () {
    $('form').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            username: {
                message: '用户名验证失败',
                validators: {
                    notEmpty: {
                        message: '用户名不能为空'
                    },
                    stringLength: {
                        min: 5,
                        max: 18,
                        message: '用户名长度必须在5到18位之间'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z0-9_]+$/,
                        message: '用户名只能包含大写、小写、数字和下划线'
                    }
                }
            },
            password:{
                validators: {
                    notEmpty: {
                        message: '密码不能为空'
                    },
                    regexp: {
                        regexp: /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$/,
                        message: '密码由英文字母和数字组成，长度为6到20个字符'
                    },
                    different:{
                        field:'username',
                        message:'密码不能与用户名相同'
                    }
                }
            },
            repassword:{
                validators: {
                    notEmpty: {
                        message: '密码不能为空'
                    },
                    identical:{
                        field:'password',
                        message:'两次密码不相同'
                    },
                    regexp: {
                        regexp: /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$/,
                        message: '密码由英文字母和数字组成，长度为6到20个字符'
                    },
                    different:{
                        field:'username',
                        message:'密码不能与用户名相同'
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: '邮箱地址不能为空'
                    },
                    emailAddress: {
                        message: '邮箱地址格式有误'
                    }
                }
            }
        }
    });
});