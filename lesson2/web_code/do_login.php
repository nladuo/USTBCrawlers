<?php
header("Content-type: text/html; charset=utf-8");
session_start();
if($_POST["uname"] == "nladuo" && $_POST["passwd"] == "nladuo") {
    $_SESSION['is_login']=true;
    echo "登陆成功";
}else {
    echo "登陆失败";
}

