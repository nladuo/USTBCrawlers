<?php
header("Content-type: text/html; charset=utf-8");
session_start();
if(isset($_SESSION['is_login'])) {
    echo "你看到了私密信息";
}else {
    echo "你无权限查看";
}
