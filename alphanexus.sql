-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 06, 2023 at 01:53 PM
-- Server version: 8.0.32-0ubuntu0.22.04.2
-- PHP Version: 8.1.2-1ubuntu2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alphanexus`
--

-- --------------------------------------------------------

--
-- Table structure for table `Build`
--

CREATE TABLE `Build` (
  `BuildID` int UNSIGNED NOT NULL,
  `ProductId` int UNSIGNED NOT NULL,
  `DeveloperUserId` int UNSIGNED NOT NULL,
  `Version` varchar(50) NOT NULL,
  `Date` datetime NOT NULL,
  `BuildContent` varchar(255) NOT NULL,
  `IsDemo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `CartProduct`
--

CREATE TABLE `CartProduct` (
  `CartProductID` int UNSIGNED NOT NULL,
  `UserId` int UNSIGNED NOT NULL,
  `ProductId` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `CDKey`
--

CREATE TABLE `CDKey` (
  `CDKeyID` int UNSIGNED NOT NULL,
  `Content` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ProductId` int UNSIGNED NOT NULL,
  `IsRedeemed` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Check`
--

CREATE TABLE `Check` (
  `CheckID` int UNSIGNED NOT NULL,
  `UserId` int UNSIGNED NOT NULL,
  `Total` decimal(10,2) NOT NULL,
  `IsRefunded` tinyint(1) DEFAULT NULL,
  `Date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `CheckProduct`
--

CREATE TABLE `CheckProduct` (
  `CheckProductID` int UNSIGNED NOT NULL,
  `CheckId` int UNSIGNED NOT NULL,
  `ProductId` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Contest`
--

CREATE TABLE `Contest` (
  `ContestID` int UNSIGNED NOT NULL,
  `ContestName` varchar(100) NOT NULL,
  `ContestImage` varchar(255) DEFAULT NULL,
  `StartDate` datetime NOT NULL,
  `EndDate` datetime NOT NULL,
  `DeveloperWinner` int UNSIGNED DEFAULT NULL,
  `DevMoneyReward` decimal(10,2) UNSIGNED DEFAULT NULL,
  `ContestDescription` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Contest`
--

INSERT INTO `Contest` (`ContestID`, `ContestName`, `ContestImage`, `StartDate`, `EndDate`, `DeveloperWinner`, `DevMoneyReward`, `ContestDescription`) VALUES
(1, 'asdasd', 'asdasd', '2022-02-21 21:14:27', '2022-02-24 21:14:27', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `ContestGame`
--

CREATE TABLE `ContestGame` (
  `ContestGameID` int UNSIGNED NOT NULL,
  `ContestId` int UNSIGNED NOT NULL,
  `GameId` int UNSIGNED NOT NULL,
  `VoteCount` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ContestPost`
--

CREATE TABLE `ContestPost` (
  `ContestPostID` int UNSIGNED NOT NULL,
  `ContestId` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `ContestPost`
--

INSERT INTO `ContestPost` (`ContestPostID`, `ContestId`) VALUES
(33, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Country`
--

CREATE TABLE `Country` (
  `CountryID` int UNSIGNED NOT NULL,
  `CountryName` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `CountryCode` varchar(2) NOT NULL,
  `CountryFlagImage` varchar(255) DEFAULT NULL,
  `Region` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Country`
--

INSERT INTO `Country` (`CountryID`, `CountryName`, `CountryCode`, `CountryFlagImage`, `Region`) VALUES
(1, 'Abkhazia', 'AB', '', ''),
(2, 'Australia', 'AU', '', ''),
(3, 'Austria', 'AT', '', ''),
(4, 'Azerbaijan', 'AZ', '', ''),
(5, 'Albania', 'AL', '', ''),
(6, 'Algeria', 'DZ', '', ''),
(7, 'American Samoa', 'AS', '', ''),
(8, 'Anguilla', 'AI', '', ''),
(9, 'Angola', 'AO', '', ''),
(10, 'Andorra', 'AD', '', ''),
(11, 'Antarctica', 'AQ', '', ''),
(12, 'Antigua and Barbuda', 'AG', '', ''),
(13, 'Argentina', 'AR', '', ''),
(14, 'Armenia', 'AM', '', ''),
(15, 'Aruba', 'AW', '', ''),
(16, 'Afghanistan', 'AF', '', ''),
(17, 'Bahamas', 'BS', '', ''),
(18, 'Bangladesh', 'BD', '', ''),
(19, 'Barbados', 'BB', '', ''),
(20, 'Bahrain', 'BH', '', ''),
(21, 'Belarus', 'BY', '', ''),
(22, 'Belize', 'BZ', '', ''),
(23, 'Belgium', 'BE', '', ''),
(24, 'Benin', 'BJ', '', ''),
(25, 'Bermuda', 'BM', '', ''),
(26, 'Bulgaria', 'BG', '', ''),
(27, 'Bolivia plurinational state of', 'BO', '', ''),
(28, 'Bonaire Sint Eustatius and Saba', 'BQ', '', ''),
(29, 'Bosnia and Herzegovina', 'BA', '', ''),
(30, 'Botswana', 'BW', '', ''),
(31, 'Brazil', 'BR', '', ''),
(32, 'British Indian Ocean Territory', 'IO', '', ''),
(33, 'Brunei Darussalam', 'BN', '', ''),
(34, 'Burkina Faso', 'BF', '', ''),
(35, 'Burundi', 'BI', '', ''),
(36, 'Bhutan', 'BT', '', ''),
(37, 'Vanuatu', 'VU', '', ''),
(38, 'Hungary', 'HU', '', ''),
(39, 'Venezuela', 'VE', '', ''),
(40, 'Virgin Islands British', 'VG', '', ''),
(41, 'Gabon', 'GA', '', ''),
(42, 'Haiti', 'HT', '', ''),
(43, 'Guyana', 'GY', '', ''),
(44, 'Gambia', 'GM', '', ''),
(45, 'Ghana', 'GH', '', ''),
(46, 'Guadeloupe', 'GP', '', ''),
(47, 'Guatemala', 'GT', '', ''),
(48, 'Guinea', 'GN', '', ''),
(49, 'Germany', 'DE', '', ''),
(50, 'Guernsey', 'GG', '', ''),
(51, 'Gibraltar', 'GI', '', ''),
(52, 'Honduras', 'HN', '', ''),
(53, 'Hong Kong', 'HK', '', ''),
(54, 'Grenada', 'GD', '', ''),
(55, 'Greenland', 'GL', '', ''),
(56, 'Greece', 'GR', '', ''),
(57, 'Georgia', 'GE', '', ''),
(58, 'Guam', 'GU', '', ''),
(59, 'Denmark', 'DK', '', ''),
(60, 'Jersey', 'JE', '', ''),
(61, 'Djibouti', 'DJ', '', ''),
(62, 'Dominica', 'DM', '', ''),
(63, 'Dominican Republic', 'DO', '', ''),
(64, 'Egypt', 'EG', '', ''),
(65, 'Zambia', 'ZM', '', ''),
(66, 'Western Sahara', 'EH', '', ''),
(67, 'Zimbabwe', 'ZW', '', ''),
(68, 'Israel', 'IL', '', ''),
(69, 'India', 'IN', '', ''),
(70, 'Indonesia', 'ID', '', ''),
(71, 'Jordan', 'JO', '', ''),
(72, 'Iraq', 'IQ', '', ''),
(73, 'Ireland', 'IE', '', ''),
(74, 'Iceland', 'IS', '', ''),
(75, 'Spain', 'ES', '', ''),
(76, 'Italy', 'IT', '', ''),
(77, 'Yemen', 'YE', '', ''),
(78, 'Cape Verde', 'CV', '', ''),
(79, 'Kazakhstan', 'KZ', '', ''),
(80, 'Cambodia', 'KH', '', ''),
(81, 'Cameroon', 'CM', '', ''),
(82, 'Canada', 'CA', '', ''),
(83, 'Qatar', 'QA', '', ''),
(84, 'Kenya', 'KE', '', ''),
(85, 'Cyprus', 'CY', '', ''),
(86, 'Kyrgyzstan', 'KG', '', ''),
(87, 'Kiribati', 'KI', '', ''),
(88, 'China', 'CN', '', ''),
(89, 'Colombia', 'CO', '', ''),
(90, 'Comoros', 'KM', '', ''),
(91, 'Congo', 'CG', '', ''),
(92, 'Costa Rica', 'CR', '', ''),
(93, 'Cuba', 'CU', '', ''),
(94, 'Kuwait', 'KW', '', ''),
(95, 'Curaçao', 'CW', '', ''),
(96, 'Latvia', 'LV', '', ''),
(97, 'Lesotho', 'LS', '', ''),
(98, 'Lebanon', 'LB', '', ''),
(99, 'Libyan Arab Jamahiriya', 'LY', '', ''),
(100, 'Liberia', 'LR', '', ''),
(101, 'Liechtenstein', 'LI', '', ''),
(102, 'Lithuania', 'LT', '', ''),
(103, 'Luxembourg', 'LU', '', ''),
(104, 'Mauritius', 'MU', '', ''),
(105, 'Mauritania', 'MR', '', ''),
(106, 'Madagascar', 'MG', '', ''),
(107, 'Mayotte', 'YT', '', ''),
(108, 'Macao', 'MO', '', ''),
(109, 'Malawi', 'MW', '', ''),
(110, 'Malaysia', 'MY', '', ''),
(111, 'Mali', 'ML', '', ''),
(112, 'United States Minor Outlying Islands', 'UM', '', ''),
(113, 'Maldives', 'MV', '', ''),
(114, 'Malta', 'MT', '', ''),
(115, 'Morocco', 'MA', '', ''),
(116, 'Martinique', 'MQ', '', ''),
(117, 'Marshall Islands', 'MH', '', ''),
(118, 'Mexico', 'MX', '', ''),
(119, 'Mozambique', 'MZ', '', ''),
(120, 'Moldova', 'MD', '', ''),
(121, 'Monaco', 'MC', '', ''),
(122, 'Mongolia', 'MN', '', ''),
(123, 'Montserrat', 'MS', '', ''),
(124, 'Myanmar', 'MM', '', ''),
(125, 'Namibia', 'NA', '', ''),
(126, 'Nauru', 'NR', '', ''),
(127, 'Nepal', 'NP', '', ''),
(128, 'Niger', 'NE', '', ''),
(129, 'Nigeria', 'NG', '', ''),
(130, 'Netherlands', 'NL', '', ''),
(131, 'Nicaragua', 'NI', '', ''),
(132, 'Niue', 'NU', '', ''),
(133, 'New Zealand', 'NZ', '', ''),
(134, 'New Caledonia', 'NC', '', ''),
(135, 'Norway', 'NO', '', ''),
(136, 'United Arab Emirates', 'AE', '', ''),
(137, 'Oman', 'OM', '', ''),
(138, 'Bouvet Island', 'BV', '', ''),
(139, 'Isle of Man', 'IM', '', ''),
(140, 'Norfolk Island', 'NF', '', ''),
(141, 'Christmas Island', 'CX', '', ''),
(142, 'Heard Island and McDonald Islands', 'HM', '', ''),
(143, 'Cayman Islands', 'KY', '', ''),
(144, 'Cook Islands', 'CK', '', ''),
(145, 'Turks and Caicos Islands', 'TC', '', ''),
(146, 'Pakistan', 'PK', '', ''),
(147, 'Palau', 'PW', '', ''),
(148, 'Palestinian Territory Occupied', 'PS', '', ''),
(149, 'Panama', 'PA', '', ''),
(150, 'Papua New Guinea', 'PG', '', ''),
(151, 'Paraguay', 'PY', '', ''),
(152, 'Peru', 'PE', '', ''),
(153, 'Pitcairn', 'PN', '', ''),
(154, 'Poland', 'PL', '', ''),
(155, 'Portugal', 'PT', '', ''),
(156, 'Puerto Rico', 'PR', '', ''),
(157, 'Reunion', 'RE', '', ''),
(158, 'Russian Federation', 'RU', '', ''),
(159, 'Rwanda', 'RW', '', ''),
(160, 'Romania', 'RO', '', ''),
(161, 'Samoa', 'WS', '', ''),
(162, 'San Marino', 'SM', '', ''),
(163, 'Sao Tome and Principe', 'ST', '', ''),
(164, 'Saudi Arabia', 'SA', '', ''),
(165, 'Swaziland', 'SZ', '', ''),
(166, 'Saint Helena Ascension And Tristan Da Cunha', 'SH', '', ''),
(167, 'Northern Mariana Islands', 'MP', '', ''),
(168, 'Saint Barthélemy', 'BL', '', ''),
(169, 'Senegal', 'SN', '', ''),
(170, 'Saint Vincent and the Grenadines', 'VC', '', ''),
(171, 'Saint Lucia', 'LC', '', ''),
(172, 'Saint Kitts and Nevis', 'KN', '', ''),
(173, 'Saint Pierre and Miquelon', 'PM', '', ''),
(174, 'Serbia', 'RS', '', ''),
(175, 'Seychelles', 'SC', '', ''),
(176, 'Singapore', 'SG', '', ''),
(177, 'Sint Maarten', 'SX', '', ''),
(178, 'Syrian Arab Republic', 'SY', '', ''),
(179, 'Slovakia', 'SK', '', ''),
(180, 'Slovenia', 'SI', '', ''),
(181, 'United Kingdom', 'GB', '', ''),
(182, 'United States', 'US', '', ''),
(183, 'Solomon Islands', 'SB', '', ''),
(184, 'Somalia', 'SO', '', ''),
(185, 'Sudan', 'SD', '', ''),
(186, 'Suriname', 'SR', '', ''),
(187, 'Sierra Leone', 'SL', '', ''),
(188, 'Tajikistan', 'TJ', '', ''),
(189, 'Thailand', 'TH', '', ''),
(190, 'Taiwan Province of China', 'TW', '', ''),
(191, 'Timor-Leste', 'TL', '', ''),
(192, 'Togo', 'TG', '', ''),
(193, 'Tokelau', 'TK', '', ''),
(194, 'Tonga', 'TO', '', ''),
(195, 'Trinidad and Tobago', 'TT', '', ''),
(196, 'Tuvalu', 'TV', '', ''),
(197, 'Tunisia', 'TN', '', ''),
(198, 'Turkmenistan', 'TM', '', ''),
(199, 'Turkey', 'TR', '', ''),
(200, 'Uganda', 'UG', '', ''),
(201, 'Uzbekistan', 'UZ', '', ''),
(202, 'Ukraine', 'UA', '', ''),
(203, 'Wallis and Futuna', 'WF', '', ''),
(204, 'Uruguay', 'UY', '', ''),
(205, 'Faroe Islands', 'FO', '', ''),
(206, 'Fiji', 'FJ', '', ''),
(207, 'Philippines', 'PH', '', ''),
(208, 'Finland', 'FI', '', ''),
(209, 'France', 'FR', '', ''),
(210, 'French Guiana', 'GF', '', ''),
(211, 'French Polynesia', 'PF', '', ''),
(212, 'French Southern Territories', 'TF', '', ''),
(213, 'Croatia', 'HR', '', ''),
(214, 'Central African Republic', 'CF', '', ''),
(215, 'Chad', 'TD', '', ''),
(216, 'Montenegro', 'ME', '', ''),
(217, 'Czech Republic', 'CZ', '', ''),
(218, 'Chile', 'CL', '', ''),
(219, 'Switzerland', 'CH', '', ''),
(220, 'Sweden', 'SE', '', ''),
(221, 'Svalbard and Jan Mayen', 'SJ', '', ''),
(222, 'Sri Lanka', 'LK', '', ''),
(223, 'Ecuador', 'EC', '', ''),
(224, 'Equatorial Guinea', 'GQ', '', ''),
(225, 'Åland Islands', 'AX', '', ''),
(226, 'El Salvador', 'SV', '', ''),
(227, 'Eritrea', 'ER', '', ''),
(228, 'Estonia', 'EE', '', ''),
(229, 'Ethiopia', 'ET', '', ''),
(230, 'South Africa', 'ZA', '', ''),
(231, 'South Georgia and the South Sandwich Islands', 'GS', '', ''),
(232, 'South Ossetia', 'OS', '', ''),
(233, 'South Sudan', 'SS', '', ''),
(234, 'Jamaica', 'JM', '', ''),
(235, 'Japan', 'JP', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `Developer`
--

CREATE TABLE `Developer` (
  `DeveloperID` int UNSIGNED NOT NULL,
  `DeveloperName` varchar(100) NOT NULL,
  `DeveloperLogo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `DeveloperBankInfo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `DeveloperYoutube` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `DeveloperTwitch` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `DeveloperBio` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `CountryId` int UNSIGNED NOT NULL,
  `Rating` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Developer`
--

INSERT INTO `Developer` (`DeveloperID`, `DeveloperName`, `DeveloperLogo`, `DeveloperBankInfo`, `DeveloperYoutube`, `DeveloperTwitch`, `DeveloperBio`, `CountryId`, `Rating`) VALUES
(6, 'Milka Games', NULL, '.', NULL, NULL, NULL, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `DeveloperUser`
--

CREATE TABLE `DeveloperUser` (
  `DeveloperUserID` int UNSIGNED NOT NULL,
  `DeveloperUserName` varchar(50) NOT NULL,
  `DeveloperUserPass` varchar(50) NOT NULL,
  `DeveloperUserEmail` varchar(255) NOT NULL,
  `DeveloperUserGuardCode` varchar(6) DEFAULT NULL,
  `DeveloperId` int UNSIGNED DEFAULT NULL,
  `DeveloperUserRole` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `LibraryItem`
--

CREATE TABLE `LibraryItem` (
  `LibraryItemID` int UNSIGNED NOT NULL,
  `UserId` int UNSIGNED NOT NULL,
  `ProductId` int UNSIGNED NOT NULL,
  `CDKeyId` int UNSIGNED NOT NULL,
  `Hours` float UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `NewsArticle`
--

CREATE TABLE `NewsArticle` (
  `NewsArticleID` int UNSIGNED NOT NULL,
  `PublisherId` int UNSIGNED NOT NULL,
  `DeveloperId` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Post`
--

CREATE TABLE `Post` (
  `PostID` int UNSIGNED NOT NULL,
  `AuthorUserId` int UNSIGNED DEFAULT NULL,
  `AuthorDevUserId` int UNSIGNED DEFAULT NULL,
  `ProductId` int UNSIGNED NOT NULL,
  `PostDate` datetime NOT NULL,
  `Header` varchar(255) NOT NULL,
  `TextContent` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Post`
--

INSERT INTO `Post` (`PostID`, `AuthorUserId`, `AuthorDevUserId`, `ProductId`, `PostDate`, `Header`, `TextContent`) VALUES
(33, 5, NULL, 16, '2004-02-20 23:00:00', 'What is this', 'asdasdasdasd');

-- --------------------------------------------------------

--
-- Table structure for table `PostComment`
--

CREATE TABLE `PostComment` (
  `PostCommentID` int UNSIGNED NOT NULL,
  `UserId` int UNSIGNED DEFAULT NULL,
  `DevUserId` int UNSIGNED DEFAULT NULL,
  `PostId` int UNSIGNED NOT NULL,
  `Content` varchar(255) NOT NULL,
  `ReplyToCommentId` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `PostCommentMedia`
--

CREATE TABLE `PostCommentMedia` (
  `PostCommentMediaID` int UNSIGNED NOT NULL,
  `PostCommentId` int UNSIGNED NOT NULL,
  `MediaContent` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `PostMedia`
--

CREATE TABLE `PostMedia` (
  `PostMediaID` int UNSIGNED NOT NULL,
  `PostId` int UNSIGNED NOT NULL,
  `MediaContent` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Product`
--

CREATE TABLE `Product` (
  `ProductID` int UNSIGNED NOT NULL,
  `Name` varchar(100) NOT NULL,
  `ReleaseDate` datetime NOT NULL,
  `DeveloperId` int UNSIGNED NOT NULL,
  `PublisherId` int UNSIGNED NOT NULL,
  `Discount` int DEFAULT NULL,
  `ShortBio` text NOT NULL,
  `About` mediumtext NOT NULL,
  `DiscountStartDate` date DEFAULT NULL,
  `DiscountEndDate` date DEFAULT NULL,
  `ReviewRating` float UNSIGNED NOT NULL,
  `TotalReviews` int UNSIGNED NOT NULL,
  `PatreonURL` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Product`
--

INSERT INTO `Product` (`ProductID`, `Name`, `ReleaseDate`, `DeveloperId`, `PublisherId`, `Discount`, `ShortBio`, `About`, `DiscountStartDate`, `DiscountEndDate`, `ReviewRating`, `TotalReviews`, `PatreonURL`) VALUES
(16, 'Return of the Obinigan', '2023-02-04 12:38:27', 6, 1, NULL, '.', '.', NULL, NULL, 0, 0, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `ProductMedia`
--

CREATE TABLE `ProductMedia` (
  `ProductMediaID` int UNSIGNED NOT NULL,
  `ProductId` int UNSIGNED NOT NULL,
  `MediaContent` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ProductPriceList`
--

CREATE TABLE `ProductPriceList` (
  `PriceListID` int UNSIGNED NOT NULL,
  `ProductId` int UNSIGNED NOT NULL,
  `Price` float UNSIGNED NOT NULL,
  `Currency` varchar(25) NOT NULL,
  `Region` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ProductTag`
--

CREATE TABLE `ProductTag` (
  `ProductTagID` int NOT NULL,
  `ProductId` int UNSIGNED NOT NULL,
  `TagId` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Publisher`
--

CREATE TABLE `Publisher` (
  `PublisherID` int UNSIGNED NOT NULL,
  `PublisherName` varchar(50) NOT NULL,
  `PublisherLogo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Publisher`
--

INSERT INTO `Publisher` (`PublisherID`, `PublisherName`, `PublisherLogo`) VALUES
(1, 'Garniere Games', ''),
(3, 'Ursula Entertainment', ''),
(5, 'Copenhagen', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `Review`
--

CREATE TABLE `Review` (
  `ReviewID` int UNSIGNED NOT NULL,
  `Rating` int UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `SystemRequirement`
--

CREATE TABLE `SystemRequirement` (
  `SystemRequirementID` int UNSIGNED NOT NULL,
  `ProductId` int UNSIGNED NOT NULL,
  `IsMinimumRecommended` tinyint(1) NOT NULL,
  `OS` varchar(30) NOT NULL,
  `CPU` varchar(50) NOT NULL,
  `RAM` varchar(10) NOT NULL,
  `GPU` varchar(50) NOT NULL,
  `DirectX` varchar(50) NOT NULL,
  `Storage` int NOT NULL,
  `SoundCard` varchar(50) NOT NULL,
  `Network` varchar(50) NOT NULL,
  `AdditionalNotes` varchar(1000) NOT NULL,
  `Platform` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Tag`
--

CREATE TABLE `Tag` (
  `TagID` int UNSIGNED NOT NULL,
  `Name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Tag`
--

INSERT INTO `Tag` (`TagID`, `Name`) VALUES
(1, 'Action'),
(2, 'Adventure'),
(3, 'Casual'),
(4, 'Simulation'),
(5, 'RPG'),
(6, 'Strategy'),
(7, 'Singleplayer'),
(8, 'Early Access'),
(9, 'Free to Play'),
(10, '2D'),
(13, 'Atmospheric'),
(14, 'Violent'),
(15, 'Massively multiplayer'),
(16, 'Sports'),
(17, '3D'),
(18, 'Multiplayer'),
(19, 'Puzzle'),
(20, 'Story Rich'),
(21, 'Fantasy'),
(22, 'Pixel Graphics'),
(23, 'Colorful'),
(24, 'Racing'),
(25, 'Exploration'),
(26, 'Cute'),
(27, 'Gore'),
(28, 'First-Person'),
(29, 'First-Person'),
(30, 'Anime'),
(31, 'Funny'),
(32, 'Sci-fi'),
(33, 'Arcade'),
(34, 'Shooter'),
(35, 'Horror'),
(36, 'Family Friendly'),
(37, 'Retro'),
(38, 'Relaxing'),
(39, 'Action-Adventure'),
(40, 'Open World'),
(41, 'Platformer'),
(42, 'Combat'),
(43, 'Co-op'),
(44, 'Great Soundtrack'),
(45, 'Female Protagonist'),
(46, 'Survival'),
(47, 'Third Person'),
(48, 'Difficult'),
(49, 'VR'),
(50, 'Comedy'),
(51, 'Stylized'),
(52, 'PvP'),
(53, 'Old School'),
(54, 'FPS'),
(55, 'Choices Matter'),
(56, 'Visual Novel'),
(57, 'Controller'),
(58, 'Realistic'),
(59, 'Online Co-op'),
(60, 'Physics'),
(61, 'Top-Down'),
(62, 'Dark'),
(63, 'Character Customization'),
(64, 'Mystery'),
(65, 'Cartoony'),
(66, 'Sandbox'),
(67, 'Multiple Endings'),
(68, 'Psychological Horror'),
(69, '2D Platformer'),
(70, 'Tactical'),
(71, 'PvE'),
(72, 'Linear'),
(73, 'Space'),
(74, 'Building'),
(75, 'Magic'),
(76, 'Point & Click'),
(77, 'Futuristic'),
(78, 'Local Multiplayer'),
(79, 'Action RPG'),
(80, 'Management'),
(81, 'Medieval'),
(82, 'Hand-drawn'),
(83, 'Crafting'),
(84, 'Turn-Based'),
(85, 'Education'),
(86, 'Procedural Generation'),
(87, 'Puzzle Platformer'),
(88, 'Replay Value'),
(89, 'Mature'),
(90, 'Survival Horror'),
(91, 'Resource Management'),
(92, 'Logic'),
(93, 'Zombies'),
(94, 'War'),
(95, 'Drama'),
(96, 'Dark Fantasy'),
(97, 'Roguelike'),
(98, 'Turn-Based Combat'),
(99, 'Turn-Based Strategy'),
(100, 'Local Co-op'),
(101, '3D Platformer'),
(102, 'Hack and Slash'),
(103, 'Romance'),
(104, 'Post-apocalyptic'),
(105, 'Base Building'),
(106, 'Turn-Based Tactics'),
(107, 'Historical'),
(108, 'Dating Sim'),
(109, 'Interactive Fiction'),
(110, 'JRPG'),
(111, 'Stealth'),
(112, 'Memes'),
(113, 'Surreal'),
(114, 'Walking Simulator'),
(115, 'Emotional'),
(116, 'Party-Based RPG'),
(117, 'Narration'),
(118, 'Dungeon Crawler'),
(119, 'Military'),
(120, 'Immersive Sim'),
(121, 'Classic'),
(122, 'Fast-Paced'),
(123, 'Third-Person Shooter'),
(124, 'Cyberpunk'),
(125, 'Steampunk'),
(126, 'Robots'),
(127, 'Short'),
(128, 'Long'),
(129, 'Top-Down Shooter'),
(130, 'Team-Based'),
(131, 'RTS'),
(132, 'Text-Based'),
(133, '2.5D'),
(134, 'Aliens'),
(135, 'Dark Humor'),
(136, 'Cinematic'),
(137, 'LGBTQ+'),
(138, 'Investigation'),
(139, 'Economy'),
(140, 'Driving'),
(141, 'Action Roguelike'),
(142, 'Card Game'),
(143, 'Abstract'),
(144, 'Experimental'),
(145, 'Nonlinear'),
(146, 'NSFW'),
(147, 'Artificial Intelligence'),
(148, '4 Player Local'),
(149, 'Inventory Management'),
(150, 'Clicker'),
(151, 'Demons'),
(152, 'Modern'),
(153, 'Thriller'),
(154, 'Psychological'),
(155, 'Detective'),
(156, 'Arena Shooter'),
(157, 'Lore-Rich'),
(158, 'Moddable'),
(159, 'Dystopian'),
(160, 'City Builer'),
(161, 'Time Management'),
(162, 'Destruction'),
(163, 'Psychedelic'),
(164, 'Competitive'),
(165, 'Precision Platformer'),
(166, 'Loot'),
(167, 'Looter Shooter'),
(168, 'Supernatural'),
(169, 'Level Editor'),
(170, 'Souls-like'),
(171, 'MMORPG'),
(172, 'Crime'),
(173, 'Parkour'),
(174, 'Mythology'),
(175, 'Dark Comedy'),
(176, 'Runner'),
(177, '2D Fighter'),
(178, 'World War II'),
(179, 'Philosophical'),
(180, 'CRPG'),
(181, 'Co-op Campaign'),
(182, 'Science'),
(183, 'Class-Based'),
(184, 'Space Sim'),
(185, 'Rhythm'),
(186, 'Blood'),
(187, 'Swordplay'),
(188, 'Gun Customization'),
(189, 'Lovecraftian'),
(190, 'Battle Royale'),
(191, 'Split Screen'),
(192, 'Vehicular Combat'),
(193, 'Open World Survival Craft'),
(194, 'Parody'),
(195, 'Noir'),
(196, 'Conspiracy'),
(197, '3D Fighter'),
(198, 'Satire'),
(199, 'Buller Time'),
(200, 'Trading'),
(201, 'Voxel'),
(202, 'Political'),
(203, 'Automation'),
(204, 'Real-Time'),
(205, 'Mouse only'),
(206, 'Colony Sim'),
(207, 'Time Manipulation'),
(208, 'Underground'),
(209, 'Time Travel'),
(210, 'Gothic'),
(211, 'Agriculture'),
(212, 'Hunting'),
(213, 'Mining'),
(214, 'Quick-Time Events'),
(215, 'MOBA'),
(216, 'Farming Sim'),
(217, 'Hero Shooter'),
(218, 'Martial Arts'),
(219, 'Tanks'),
(220, 'Ninja'),
(221, 'Pirates'),
(222, 'Hacking'),
(223, 'Remake'),
(224, 'Combat Racing'),
(225, 'Cold War'),
(226, 'Fishing'),
(227, 'Superhero'),
(228, 'Assassin'),
(229, 'Programming'),
(230, 'Dinosaurs'),
(231, 'Underwater'),
(232, 'Vampire'),
(233, 'Naval'),
(234, 'Trains'),
(235, 'Immersive'),
(236, 'Cooking'),
(237, 'Narrative'),
(238, 'Heist'),
(239, 'Western'),
(240, 'Faith'),
(241, 'Minigames'),
(242, 'Political Sim'),
(243, 'Party'),
(244, 'Archery'),
(245, 'Diplomacy'),
(246, 'Party Game'),
(247, 'Snow'),
(248, 'Naval Combat'),
(249, 'Dungeons & Dragons'),
(250, 'Sniper'),
(251, 'Gambling'),
(252, 'Villain Protagonist'),
(253, 'Typing'),
(254, 'Mars'),
(255, 'Moon'),
(256, 'Documentary'),
(257, 'Soccer'),
(258, 'Football'),
(259, 'World War I'),
(260, 'On-Rails Shooter'),
(261, 'Werewolves'),
(262, 'Vampires'),
(263, 'Trivia'),
(264, 'Silent Protagonist'),
(265, 'Unforgiving'),
(266, 'Jet'),
(267, 'Rome'),
(268, 'Spaceships'),
(269, 'Motorbike'),
(270, 'Vikings'),
(271, 'Tennis'),
(272, 'Baseball'),
(273, 'Skating'),
(274, 'Hockey'),
(275, 'Bowling'),
(276, 'Tabletop');

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE `User` (
  `UserID` int UNSIGNED NOT NULL,
  `UserName` varchar(30) NOT NULL,
  `UserPassword` varchar(50) NOT NULL,
  `UserEmail` varchar(255) NOT NULL,
  `UserPhone` varchar(20) NOT NULL,
  `UserAvatar` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `ProfileBackground` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `IsPrivate` tinyint(1) DEFAULT NULL,
  `StatusId` int UNSIGNED DEFAULT NULL,
  `UserRealName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `UserCountryId` int UNSIGNED DEFAULT NULL,
  `Bio` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `EmailSubscription` tinyint(1) DEFAULT NULL,
  `LastOnline` datetime DEFAULT NULL,
  `UserBotToken` varchar(51) DEFAULT NULL,
  `CashbackBonus` int UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `User`
--

INSERT INTO `User` (`UserID`, `UserName`, `UserPassword`, `UserEmail`, `UserPhone`, `UserAvatar`, `ProfileBackground`, `IsPrivate`, `StatusId`, `UserRealName`, `UserCountryId`, `Bio`, `EmailSubscription`, `LastOnline`, `UserBotToken`, `CashbackBonus`) VALUES
(5, 'aleksei', 'admin', 'alexlapchik@mail.ru', '89856495003', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2023-02-04 12:33:29', NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `UserLike`
--

CREATE TABLE `UserLike` (
  `UserLikeID` int UNSIGNED NOT NULL,
  `UserId` int UNSIGNED NOT NULL,
  `PostId` int UNSIGNED DEFAULT NULL,
  `CommentId` int UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `UserNewsPreference`
--

CREATE TABLE `UserNewsPreference` (
  `UserNewsPreferenceID` int UNSIGNED NOT NULL,
  `UserId` int UNSIGNED NOT NULL,
  `DeveloperId` int UNSIGNED DEFAULT NULL,
  `PublisherId` int UNSIGNED DEFAULT NULL,
  `ProductId` int UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `UserVote`
--

CREATE TABLE `UserVote` (
  `UserVoteID` int UNSIGNED NOT NULL,
  `UserId` int UNSIGNED NOT NULL,
  `ContestPostId` int UNSIGNED DEFAULT NULL,
  `ContestGameId` int UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `WishlistProduct`
--

CREATE TABLE `WishlistProduct` (
  `WishlistProductID` int UNSIGNED NOT NULL,
  `UserId` int UNSIGNED NOT NULL,
  `ProductId` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Build`
--
ALTER TABLE `Build`
  ADD PRIMARY KEY (`BuildID`),
  ADD KEY `FK_ProductBuild` (`ProductId`),
  ADD KEY `FK_DevUserBuild` (`DeveloperUserId`);

--
-- Indexes for table `CartProduct`
--
ALTER TABLE `CartProduct`
  ADD PRIMARY KEY (`CartProductID`),
  ADD KEY `FK_CartProduct` (`ProductId`),
  ADD KEY `FK_CartUser` (`UserId`);

--
-- Indexes for table `CDKey`
--
ALTER TABLE `CDKey`
  ADD PRIMARY KEY (`CDKeyID`),
  ADD KEY `FK_ProductCDKey` (`ProductId`);

--
-- Indexes for table `Check`
--
ALTER TABLE `Check`
  ADD PRIMARY KEY (`CheckID`),
  ADD KEY `FK_CheckUser` (`UserId`);

--
-- Indexes for table `CheckProduct`
--
ALTER TABLE `CheckProduct`
  ADD PRIMARY KEY (`CheckProductID`),
  ADD KEY `FK_CheckProductCheck` (`CheckId`),
  ADD KEY `FK_ProductProductCheck` (`ProductId`);

--
-- Indexes for table `Contest`
--
ALTER TABLE `Contest`
  ADD PRIMARY KEY (`ContestID`),
  ADD KEY `FK_DevWinner` (`DeveloperWinner`);

--
-- Indexes for table `ContestGame`
--
ALTER TABLE `ContestGame`
  ADD PRIMARY KEY (`ContestGameID`),
  ADD KEY `FK_ContestContestGame` (`ContestId`),
  ADD KEY `FK_GameContestGame` (`GameId`);

--
-- Indexes for table `ContestPost`
--
ALTER TABLE `ContestPost`
  ADD KEY `FK_ContestPost` (`ContestPostID`),
  ADD KEY `FK_ContestContestPost` (`ContestId`);

--
-- Indexes for table `Country`
--
ALTER TABLE `Country`
  ADD PRIMARY KEY (`CountryID`);

--
-- Indexes for table `Developer`
--
ALTER TABLE `Developer`
  ADD PRIMARY KEY (`DeveloperID`),
  ADD KEY `FK_DevCountry` (`CountryId`);

--
-- Indexes for table `DeveloperUser`
--
ALTER TABLE `DeveloperUser`
  ADD PRIMARY KEY (`DeveloperUserID`),
  ADD KEY `FK_DevUserDeveloper` (`DeveloperId`);

--
-- Indexes for table `LibraryItem`
--
ALTER TABLE `LibraryItem`
  ADD PRIMARY KEY (`LibraryItemID`),
  ADD KEY `FK_LibraryUser` (`UserId`),
  ADD KEY `FK_LibraryCDKey` (`CDKeyId`),
  ADD KEY `FK_LibraryProduct` (`ProductId`);

--
-- Indexes for table `NewsArticle`
--
ALTER TABLE `NewsArticle`
  ADD KEY `FK_PostNews` (`NewsArticleID`),
  ADD KEY `FK_DeveloperNews` (`DeveloperId`),
  ADD KEY `FK_PublisherNews` (`PublisherId`);

--
-- Indexes for table `Post`
--
ALTER TABLE `Post`
  ADD PRIMARY KEY (`PostID`),
  ADD KEY `FK_UserAuthor` (`AuthorUserId`),
  ADD KEY `FK_DevUserAuthor` (`AuthorDevUserId`),
  ADD KEY `FK_ProductPost` (`ProductId`);

--
-- Indexes for table `PostComment`
--
ALTER TABLE `PostComment`
  ADD PRIMARY KEY (`PostCommentID`),
  ADD KEY `FK_PostCommentUser` (`UserId`),
  ADD KEY `FK_PostCommentDevUser` (`DevUserId`),
  ADD KEY `FK_PostCommentPost` (`PostId`),
  ADD KEY `FK_CommentComment` (`ReplyToCommentId`);

--
-- Indexes for table `PostCommentMedia`
--
ALTER TABLE `PostCommentMedia`
  ADD PRIMARY KEY (`PostCommentMediaID`),
  ADD KEY `FK_CommentPostMedia` (`PostCommentId`);

--
-- Indexes for table `PostMedia`
--
ALTER TABLE `PostMedia`
  ADD PRIMARY KEY (`PostMediaID`),
  ADD KEY `FK_MediaPost` (`PostId`);

--
-- Indexes for table `Product`
--
ALTER TABLE `Product`
  ADD PRIMARY KEY (`ProductID`),
  ADD KEY `FK_ProductDeveloper` (`DeveloperId`),
  ADD KEY `FK_ProductPublisher` (`PublisherId`);

--
-- Indexes for table `ProductMedia`
--
ALTER TABLE `ProductMedia`
  ADD PRIMARY KEY (`ProductMediaID`),
  ADD KEY `FK_ProductMedia` (`ProductId`);

--
-- Indexes for table `ProductPriceList`
--
ALTER TABLE `ProductPriceList`
  ADD PRIMARY KEY (`PriceListID`),
  ADD KEY `FK_ProductPriceList` (`ProductId`);

--
-- Indexes for table `ProductTag`
--
ALTER TABLE `ProductTag`
  ADD PRIMARY KEY (`ProductTagID`),
  ADD KEY `FK_ProductProductTag` (`ProductId`),
  ADD KEY `FK_TagProductTag` (`TagId`);

--
-- Indexes for table `Publisher`
--
ALTER TABLE `Publisher`
  ADD PRIMARY KEY (`PublisherID`);

--
-- Indexes for table `Review`
--
ALTER TABLE `Review`
  ADD KEY `FK_ReviewPost` (`ReviewID`);

--
-- Indexes for table `SystemRequirement`
--
ALTER TABLE `SystemRequirement`
  ADD PRIMARY KEY (`SystemRequirementID`),
  ADD KEY `FK_ReqProduct` (`ProductId`);

--
-- Indexes for table `Tag`
--
ALTER TABLE `Tag`
  ADD PRIMARY KEY (`TagID`);

--
-- Indexes for table `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`UserID`),
  ADD KEY `FK_UserCountry` (`UserCountryId`);

--
-- Indexes for table `UserLike`
--
ALTER TABLE `UserLike`
  ADD PRIMARY KEY (`UserLikeID`),
  ADD KEY `FK_LikeUser` (`UserId`),
  ADD KEY `FK_LikeComment` (`CommentId`),
  ADD KEY `FK_LikePost` (`PostId`);

--
-- Indexes for table `UserNewsPreference`
--
ALTER TABLE `UserNewsPreference`
  ADD PRIMARY KEY (`UserNewsPreferenceID`),
  ADD KEY `FK_UserPreference` (`UserId`),
  ADD KEY `FK_DevPreference` (`DeveloperId`),
  ADD KEY `FK_PubPreference` (`PublisherId`),
  ADD KEY `FK_ProdPreference` (`ProductId`);

--
-- Indexes for table `UserVote`
--
ALTER TABLE `UserVote`
  ADD PRIMARY KEY (`UserVoteID`),
  ADD KEY `FK_Product` (`ContestGameId`),
  ADD KEY `FK_UserVote` (`UserId`),
  ADD KEY `FK_VoteContest` (`ContestPostId`);

--
-- Indexes for table `WishlistProduct`
--
ALTER TABLE `WishlistProduct`
  ADD PRIMARY KEY (`WishlistProductID`),
  ADD KEY `FK_WishlistProduct` (`ProductId`),
  ADD KEY `FK_UserProduct` (`UserId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Build`
--
ALTER TABLE `Build`
  MODIFY `BuildID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `CartProduct`
--
ALTER TABLE `CartProduct`
  MODIFY `CartProductID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `CDKey`
--
ALTER TABLE `CDKey`
  MODIFY `CDKeyID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Check`
--
ALTER TABLE `Check`
  MODIFY `CheckID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `CheckProduct`
--
ALTER TABLE `CheckProduct`
  MODIFY `CheckProductID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Contest`
--
ALTER TABLE `Contest`
  MODIFY `ContestID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `ContestGame`
--
ALTER TABLE `ContestGame`
  MODIFY `ContestGameID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `Country`
--
ALTER TABLE `Country`
  MODIFY `CountryID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=236;

--
-- AUTO_INCREMENT for table `Developer`
--
ALTER TABLE `Developer`
  MODIFY `DeveloperID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `DeveloperUser`
--
ALTER TABLE `DeveloperUser`
  MODIFY `DeveloperUserID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `LibraryItem`
--
ALTER TABLE `LibraryItem`
  MODIFY `LibraryItemID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Post`
--
ALTER TABLE `Post`
  MODIFY `PostID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `PostComment`
--
ALTER TABLE `PostComment`
  MODIFY `PostCommentID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `PostCommentMedia`
--
ALTER TABLE `PostCommentMedia`
  MODIFY `PostCommentMediaID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `PostMedia`
--
ALTER TABLE `PostMedia`
  MODIFY `PostMediaID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Product`
--
ALTER TABLE `Product`
  MODIFY `ProductID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `ProductMedia`
--
ALTER TABLE `ProductMedia`
  MODIFY `ProductMediaID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `ProductPriceList`
--
ALTER TABLE `ProductPriceList`
  MODIFY `PriceListID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `ProductTag`
--
ALTER TABLE `ProductTag`
  MODIFY `ProductTagID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `Publisher`
--
ALTER TABLE `Publisher`
  MODIFY `PublisherID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `SystemRequirement`
--
ALTER TABLE `SystemRequirement`
  MODIFY `SystemRequirementID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Tag`
--
ALTER TABLE `Tag`
  MODIFY `TagID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=299;

--
-- AUTO_INCREMENT for table `User`
--
ALTER TABLE `User`
  MODIFY `UserID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `UserLike`
--
ALTER TABLE `UserLike`
  MODIFY `UserLikeID` int UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `UserNewsPreference`
--
ALTER TABLE `UserNewsPreference`
  MODIFY `UserNewsPreferenceID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `UserVote`
--
ALTER TABLE `UserVote`
  MODIFY `UserVoteID` int UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `WishlistProduct`
--
ALTER TABLE `WishlistProduct`
  MODIFY `WishlistProductID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Build`
--
ALTER TABLE `Build`
  ADD CONSTRAINT `FK_DevUserBuild` FOREIGN KEY (`DeveloperUserId`) REFERENCES `DeveloperUser` (`DeveloperUserID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ProductBuild` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `CartProduct`
--
ALTER TABLE `CartProduct`
  ADD CONSTRAINT `FK_CartProduct` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CartUser` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `CDKey`
--
ALTER TABLE `CDKey`
  ADD CONSTRAINT `FK_ProductCDKey` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Check`
--
ALTER TABLE `Check`
  ADD CONSTRAINT `FK_CheckUser` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `CheckProduct`
--
ALTER TABLE `CheckProduct`
  ADD CONSTRAINT `FK_CheckProductCheck` FOREIGN KEY (`CheckId`) REFERENCES `Check` (`CheckID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ProductProductCheck` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Contest`
--
ALTER TABLE `Contest`
  ADD CONSTRAINT `FK_DevWinner` FOREIGN KEY (`DeveloperWinner`) REFERENCES `Developer` (`DeveloperID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ContestGame`
--
ALTER TABLE `ContestGame`
  ADD CONSTRAINT `FK_ContestContestGame` FOREIGN KEY (`ContestId`) REFERENCES `Contest` (`ContestID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_GameContestGame` FOREIGN KEY (`GameId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ContestPost`
--
ALTER TABLE `ContestPost`
  ADD CONSTRAINT `FK_ContestContestPost` FOREIGN KEY (`ContestId`) REFERENCES `Contest` (`ContestID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ContestPostPost` FOREIGN KEY (`ContestPostID`) REFERENCES `Post` (`PostID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Developer`
--
ALTER TABLE `Developer`
  ADD CONSTRAINT `FK_DevCountry` FOREIGN KEY (`CountryId`) REFERENCES `Country` (`CountryID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `DeveloperUser`
--
ALTER TABLE `DeveloperUser`
  ADD CONSTRAINT `FK_DevUserDeveloper` FOREIGN KEY (`DeveloperId`) REFERENCES `Developer` (`DeveloperID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `LibraryItem`
--
ALTER TABLE `LibraryItem`
  ADD CONSTRAINT `FK_LibraryCDKey` FOREIGN KEY (`CDKeyId`) REFERENCES `CDKey` (`CDKeyID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_LibraryProduct` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_LibraryUser` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `NewsArticle`
--
ALTER TABLE `NewsArticle`
  ADD CONSTRAINT `FK_DeveloperNews` FOREIGN KEY (`DeveloperId`) REFERENCES `Developer` (`DeveloperID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_PostNews` FOREIGN KEY (`NewsArticleID`) REFERENCES `Post` (`PostID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_PublisherNews` FOREIGN KEY (`PublisherId`) REFERENCES `Publisher` (`PublisherID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Post`
--
ALTER TABLE `Post`
  ADD CONSTRAINT `FK_DevUserAuthor` FOREIGN KEY (`AuthorDevUserId`) REFERENCES `DeveloperUser` (`DeveloperUserID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ProductPost` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_UserAuthor` FOREIGN KEY (`AuthorUserId`) REFERENCES `User` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `PostComment`
--
ALTER TABLE `PostComment`
  ADD CONSTRAINT `FK_CommentComment` FOREIGN KEY (`ReplyToCommentId`) REFERENCES `PostComment` (`PostCommentID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_PostCommentDevUser` FOREIGN KEY (`DevUserId`) REFERENCES `DeveloperUser` (`DeveloperUserID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_PostCommentPost` FOREIGN KEY (`PostId`) REFERENCES `Post` (`PostID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_PostCommentUser` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `PostCommentMedia`
--
ALTER TABLE `PostCommentMedia`
  ADD CONSTRAINT `FK_CommentPostMedia` FOREIGN KEY (`PostCommentId`) REFERENCES `PostComment` (`PostCommentID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `PostMedia`
--
ALTER TABLE `PostMedia`
  ADD CONSTRAINT `FK_MediaPost` FOREIGN KEY (`PostId`) REFERENCES `Post` (`PostID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Product`
--
ALTER TABLE `Product`
  ADD CONSTRAINT `FK_ProductDeveloper` FOREIGN KEY (`DeveloperId`) REFERENCES `Developer` (`DeveloperID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ProductPublisher` FOREIGN KEY (`PublisherId`) REFERENCES `Publisher` (`PublisherID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ProductMedia`
--
ALTER TABLE `ProductMedia`
  ADD CONSTRAINT `FK_ProductMedia` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ProductPriceList`
--
ALTER TABLE `ProductPriceList`
  ADD CONSTRAINT `FK_ProductPriceList` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ProductTag`
--
ALTER TABLE `ProductTag`
  ADD CONSTRAINT `FK_ProductProductTag` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_TagProductTag` FOREIGN KEY (`TagId`) REFERENCES `Tag` (`TagID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Review`
--
ALTER TABLE `Review`
  ADD CONSTRAINT `FK_ReviewPost` FOREIGN KEY (`ReviewID`) REFERENCES `Post` (`PostID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `SystemRequirement`
--
ALTER TABLE `SystemRequirement`
  ADD CONSTRAINT `FK_ReqProduct` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `User`
--
ALTER TABLE `User`
  ADD CONSTRAINT `FK_UserCountry` FOREIGN KEY (`UserCountryId`) REFERENCES `Country` (`CountryID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `UserLike`
--
ALTER TABLE `UserLike`
  ADD CONSTRAINT `FK_LikeComment` FOREIGN KEY (`CommentId`) REFERENCES `PostComment` (`PostCommentID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `FK_LikePost` FOREIGN KEY (`PostId`) REFERENCES `Post` (`PostID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `FK_LikeUser` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserID`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `UserNewsPreference`
--
ALTER TABLE `UserNewsPreference`
  ADD CONSTRAINT `FK_DevPreference` FOREIGN KEY (`DeveloperId`) REFERENCES `Developer` (`DeveloperID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ProdPreference` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_PubPreference` FOREIGN KEY (`PublisherId`) REFERENCES `Publisher` (`PublisherID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_UserPreference` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `UserVote`
--
ALTER TABLE `UserVote`
  ADD CONSTRAINT `FK_UserVote` FOREIGN KEY (`UserId`) REFERENCES `UserVote` (`UserVoteID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_VoteContestGame` FOREIGN KEY (`ContestGameId`) REFERENCES `ContestGame` (`ContestGameID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_VoteContestPost` FOREIGN KEY (`ContestPostId`) REFERENCES `ContestPost` (`ContestPostID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `WishlistProduct`
--
ALTER TABLE `WishlistProduct`
  ADD CONSTRAINT `FK_UserProduct` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_WishlistProduct` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
