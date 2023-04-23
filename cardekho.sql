-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 23, 2023 at 05:57 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cardekho`
--

-- --------------------------------------------------------

--
-- Table structure for table `brands`
--

CREATE TABLE `brands` (
  `brand` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `brands`
--

INSERT INTO `brands` (`brand`) VALUES
('Hyundai'),
('Kia'),
('Mahindra'),
('Maruti Suzuki'),
('Renault'),
('Skoda'),
('Tata'),
('Volkswagen');

-- --------------------------------------------------------

--
-- Table structure for table `buyc`
--

CREATE TABLE `buyc` (
  `Name` varchar(20) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `DOB` date NOT NULL,
  `Address` varchar(200) NOT NULL,
  `Aadhaar` varchar(20) NOT NULL,
  `Brand` varchar(20) NOT NULL,
  `Category` varchar(20) NOT NULL,
  `Cname` varchar(20) NOT NULL,
  `Rn` varchar(20) NOT NULL,
  `Md` date NOT NULL,
  `ft` varchar(20) NOT NULL,
  `Price` varchar(20) NOT NULL,
  `pic` varchar(100) NOT NULL,
  `avail` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `buyc`
--

INSERT INTO `buyc` (`Name`, `Phone`, `Gender`, `DOB`, `Address`, `Aadhaar`, `Brand`, `Category`, `Cname`, `Rn`, `Md`, `ft`, `Price`, `pic`, `avail`) VALUES
('mahesh', '9779230139', 'Male', '2010-02-17', 'jalmndhar\n', '987456321023', 'Maruti Suzuki', 'Hatchback', 'swift', '123', '2010-02-11', 'Diesel', '550000', '1677067628download.jfif', 1),
('monica', '1236547892', 'Female', '2010-02-03', 'jal\n', '987456302145', 'Maruti Suzuki', 'Hatchback', 'swift', 'a1', '2010-02-04', 'Diesel', '550000', '1677087965download.jfif', 0),
('aman', '98745613232', 'Male', '2010-03-03', 'jkal\n', '987456123053', 'Tata', 'SUV', 'Nexon', 'dfgert4564', '2010-02-03', 'Petrol', '700000', '1677043757download (1).jfif', 0),
('himashuy', '9464104093', 'Male', '2010-02-10', 'jal\na\n\n', '123644789502', 'Hyundai', 'Hatchback', 'i10', 'pb08bd3256', '2010-02-09', 'Petrol', '500000', '1676997037hyundai-grand-i10-nios-exterior-36.jpg', 0);

-- --------------------------------------------------------

--
-- Table structure for table `facultytable`
--

CREATE TABLE `facultytable` (
  `Name` varchar(200) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  `Address` varchar(200) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `usertype` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `facultytable`
--

INSERT INTO `facultytable` (`Name`, `Phone`, `Gender`, `dob`, `Address`, `Username`, `Password`, `usertype`) VALUES
('ram', '4542421114', 'Male', '2002-09-05', 'jh\n\n', 'a1', '123', 'Employee'),
('himanshu', '9464104093', 'Male', '2002-09-05', 'Jalandhar\n', 'him1', '123', 'Admin'),
('ritu', '94641040932552', 'Male', '2002-09-05', 'Jalandhar\nds\n\n', 'him2', '123', 'Employee');

-- --------------------------------------------------------

--
-- Table structure for table `sellc`
--

CREATE TABLE `sellc` (
  `Name` varchar(20) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `DOB` date NOT NULL,
  `Address` varchar(200) NOT NULL,
  `Aadhaar` varchar(20) NOT NULL,
  `Brand` varchar(20) NOT NULL,
  `Category` varchar(20) NOT NULL,
  `Cname` varchar(20) NOT NULL,
  `Rn` varchar(20) NOT NULL,
  `Md` date NOT NULL,
  `ft` varchar(20) NOT NULL,
  `Price` varchar(20) NOT NULL,
  `pic` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sellc`
--

INSERT INTO `sellc` (`Name`, `Phone`, `Gender`, `DOB`, `Address`, `Aadhaar`, `Brand`, `Category`, `Cname`, `Rn`, `Md`, `ft`, `Price`, `pic`) VALUES
('Gitika', '1236547892', 'Female', '2010-02-03', 'jalandhar\n\n', '987456302145', 'Maruti Suzuki', 'Hatchback', 'swift', 'a1', '2010-02-04', 'Diesel', '550000', '1677087965download.jfif'),
('monica', '9464104093', 'Female', '2010-02-10', 'jalandhar\n\n\n', '123644789502', 'Hyundai', 'Hatchback', 'i10', 'pb08bd3256', '2010-02-09', 'Petrol', '500000', '1676997037hyundai-grand-i10-nios-exterior-36.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `brands`
--
ALTER TABLE `brands`
  ADD PRIMARY KEY (`brand`);

--
-- Indexes for table `buyc`
--
ALTER TABLE `buyc`
  ADD PRIMARY KEY (`Rn`);

--
-- Indexes for table `facultytable`
--
ALTER TABLE `facultytable`
  ADD PRIMARY KEY (`Username`);

--
-- Indexes for table `sellc`
--
ALTER TABLE `sellc`
  ADD PRIMARY KEY (`Rn`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
