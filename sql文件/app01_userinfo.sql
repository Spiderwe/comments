/*
 Navicat Premium Data Transfer

 Source Server         : wcc
 Source Server Type    : MySQL
 Source Server Version : 50724
 Source Host           : localhost:3306
 Source Schema         : aboke

 Target Server Type    : MySQL
 Target Server Version : 50724
 File Encoding         : 65001

 Date: 22/03/2020 23:04:29
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for app01_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `app01_userinfo`;
CREATE TABLE `app01_userinfo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `create_time` date NOT NULL,
  `avatar` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of app01_userinfo
-- ----------------------------
INSERT INTO `app01_userinfo` VALUES (1, 'pbkdf2_sha256$36000$fGTKkoMrVTkf$KkbTqQ3uTSK+tYVRdNnzLwWZZ357WKGmIiaTlkWDwiQ=', '2020-03-18 14:27:53.543241', 0, 'tommm', '', '', '1197865477@qq.com', 0, 1, '2020-03-18 03:21:54.728332', NULL, '2020-03-18', 'avatar/222.jpg');
INSERT INTO `app01_userinfo` VALUES (2, 'pbkdf2_sha256$36000$PjUH7mrloYpN$OluiB5sw2AMimNjAGqrILsCsnmNEptFU7eQEiJvGWCw=', '2020-03-18 11:51:47.765401', 0, 'tonyy', '', '', '1197865477@qq.com', 0, 1, '2020-03-18 11:51:37.863386', NULL, '2020-03-18', 'avatar/444.jpg');

SET FOREIGN_KEY_CHECKS = 1;
