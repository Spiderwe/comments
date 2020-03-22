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

 Date: 22/03/2020 23:03:46
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for app01_comment
-- ----------------------------
DROP TABLE IF EXISTS `app01_comment`;
CREATE TABLE `app01_comment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` date NOT NULL,
  `article_id` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `app01_comment_article_id_2bf4f73b_fk_app01_article_id`(`article_id`) USING BTREE,
  INDEX `app01_comment_parent_id_a8e69cb8_fk_app01_comment_id`(`parent_id`) USING BTREE,
  INDEX `app01_comment_user_id_7f913f03_fk_app01_userinfo_id`(`user_id`) USING BTREE,
  CONSTRAINT `app01_comment_article_id_2bf4f73b_fk_app01_article_id` FOREIGN KEY (`article_id`) REFERENCES `app01_article` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `app01_comment_parent_id_a8e69cb8_fk_app01_comment_id` FOREIGN KEY (`parent_id`) REFERENCES `app01_comment` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `app01_comment_user_id_7f913f03_fk_app01_userinfo_id` FOREIGN KEY (`user_id`) REFERENCES `app01_userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of app01_comment
-- ----------------------------
INSERT INTO `app01_comment` VALUES (1, 'haha', '2020-03-18', 2, NULL, 1);
INSERT INTO `app01_comment` VALUES (2, 'ok', '2020-03-18', 2, 1, 1);

SET FOREIGN_KEY_CHECKS = 1;
