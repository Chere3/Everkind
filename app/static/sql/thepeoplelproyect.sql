-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 27, 2024 at 06:43 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `thepeoplelproyect`
--

-- --------------------------------------------------------

--
-- Table structure for table `guests`
--

CREATE TABLE `guests` (
  `id` bigint(20) NOT NULL,
  `name` text NOT NULL,
  `contact_info` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `occupants`
--

CREATE TABLE `occupants` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `room_id` bigint(20) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `guest_id` bigint(20) DEFAULT NULL,
  `name` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `occupants`
--

INSERT INTO `occupants` (`id`, `user_id`, `room_id`, `start_date`, `end_date`, `created_at`, `updated_at`, `guest_id`, `name`) VALUES
(7, 16, NULL, NULL, '2024-11-26', '2024-11-27 01:25:54', '2024-11-27 01:25:54', NULL, 'Diego  Romero Galván'),
(8, 16, NULL, NULL, NULL, '2024-11-27 04:41:51', '2024-11-27 04:41:51', NULL, 'Diego Romero Galván');

-- --------------------------------------------------------

--
-- Table structure for table `order_history`
--

CREATE TABLE `order_history` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `occupant_id` bigint(20) NOT NULL,
  `visit_id` bigint(20) DEFAULT NULL,
  `order_id` bigint(20) NOT NULL,
  `action` text NOT NULL,
  `action_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_history`
--

INSERT INTO `order_history` (`id`, `user_id`, `occupant_id`, `visit_id`, `order_id`, `action`, `action_date`, `created_at`, `updated_at`) VALUES
(2, 16, 7, NULL, 8, 'booked', '2024-11-27 02:14:44', '2024-11-27 02:14:44', '2024-11-27 02:14:44'),
(3, 16, 7, NULL, 9, 'booked', '2024-11-27 02:28:23', '2024-11-27 02:28:23', '2024-11-27 02:28:23'),
(4, 16, 7, NULL, 10, 'cancelled', '2024-11-27 02:42:28', '2024-11-27 02:42:28', '2024-11-27 02:42:28'),
(5, 16, 7, NULL, 11, 'booked', '2024-11-27 02:42:45', '2024-11-27 02:42:45', '2024-11-27 02:42:45'),
(6, 16, 7, NULL, 12, 'cancelled', '2024-11-27 02:42:53', '2024-11-27 02:42:53', '2024-11-27 02:42:53');

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` bigint(20) NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `name`) VALUES
(1, 'USER'),
(2, 'ADMIN'),
(3, 'GUEST'),
(4, 'OCCUPANT');

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `id` bigint(20) NOT NULL,
  `name` text DEFAULT NULL,
  `room_number` text NOT NULL,
  `capacity` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `room_type_id` bigint(20) DEFAULT NULL,
  `room_type_photo` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`id`, `name`, `room_number`, `capacity`, `created_at`, `updated_at`, `room_type_id`, `room_type_photo`) VALUES
(3, 'Sunflower Suite', '101', 1, '2024-11-25 17:16:31', '2024-11-25 17:16:31', 2, NULL),
(5, 'Rosewood Retreat', '234', 4, '2024-11-26 07:00:46', '2024-11-26 07:00:46', 7, NULL),
(6, 'Lavender Haven', '568', 7, '2024-11-26 07:00:46', '2024-11-26 07:00:46', 8, NULL),
(7, 'Willow Room', '59', 8, '2024-11-26 07:00:46', '2024-11-26 07:00:46', 8, NULL),
(8, 'Maple Grove', '678', 4, '2024-11-26 07:00:46', '2024-11-26 07:00:46', 5, NULL),
(9, 'Meadow View', '654', 1, '2024-11-26 07:00:46', '2024-11-26 07:00:46', 4, NULL),
(10, 'Golden Horizons', '543', 2, '2024-11-26 07:00:46', '2024-11-26 07:00:46', 5, NULL),
(11, 'Cherry Blossom Suite', '532', 10, '2024-11-26 07:00:46', '2024-11-26 07:00:46', 7, NULL),
(12, 'Morning Glory Room', '876', 3, '2024-11-26 07:00:46', '2024-11-26 07:00:46', 8, NULL),
(13, 'Oakwood Corner', '765', 3, '2024-11-26 07:00:46', '2024-11-26 07:00:46', 6, NULL),
(14, 'Silver Birch Suite', '554', 2, '2024-11-26 07:00:46', '2024-11-26 07:00:46', 2, NULL),
(15, 'Daffodil Dwelling', '998', 3, '2024-11-26 07:00:46', '2024-11-26 07:00:46', 5, NULL),
(16, 'Magnolia Manor', '1', 1, '2024-11-26 07:00:46', '2024-11-26 07:00:46', 4, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `room_orders`
--

CREATE TABLE `room_orders` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `room_id` bigint(20) NOT NULL,
  `order_date` date NOT NULL,
  `status` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room_orders`
--

INSERT INTO `room_orders` (`id`, `user_id`, `room_id`, `order_date`, `status`, `created_at`, `updated_at`) VALUES
(8, 16, 7, '2024-11-26', '1', '2024-11-27 02:14:44', '2024-11-27 02:14:44'),
(9, 16, 15, '2024-11-26', '1', '2024-11-27 02:28:23', '2024-11-27 02:28:23'),
(10, 16, 15, '2024-11-26', '0', '2024-11-27 02:42:28', '2024-11-27 02:42:28'),
(11, 16, 6, '2024-11-26', '1', '2024-11-27 02:42:45', '2024-11-27 02:42:45'),
(12, 16, 6, '2024-11-26', '0', '2024-11-27 02:42:53', '2024-11-27 02:42:53');

-- --------------------------------------------------------

--
-- Table structure for table `room_types`
--

CREATE TABLE `room_types` (
  `id` bigint(20) NOT NULL,
  `type_name` text NOT NULL,
  `description` text DEFAULT NULL,
  `photo` longtext DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room_types`
--

INSERT INTO `room_types` (`id`, `type_name`, `description`, `photo`, `created_at`, `updated_at`) VALUES
(2, 'single', 'A bright, cheerful space filled with golden accents and floral décor, symbolizing happiness and positivity. Large windows allow sunlight to flood in, creating a welcoming atmosphere.', 'https://images.pexels.com/photos/6782469/pexels-photo-6782469.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', '2024-11-25 17:15:01', '2024-11-25 17:15:01'),
(4, 'private', 'A single-occupancy room for one resident.', 'https://images.pexels.com/photos/1571453/pexels-photo-1571453.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', '2024-11-26 06:52:16', '2024-11-26 06:52:16'),
(5, 'semi-private', 'A room shared between two residents, often with a divider for privacy.', 'https://images.pexels.com/photos/813692/pexels-photo-813692.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', '2024-11-26 06:52:16', '2024-11-26 06:52:16'),
(6, 'shared', 'A room for multiple residents, typically more than two.', 'https://images.pexels.com/photos/1571459/pexels-photo-1571459.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', '2024-11-26 06:52:16', '2024-11-26 06:52:16'),
(7, 'deluxe', 'A private room with additional amenities such as extra space, a private bathroom, or upgraded furnishings.', 'https://images.pexels.com/photos/1571457/pexels-photo-1571457.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', '2024-11-26 06:52:16', '2024-11-26 06:52:16'),
(8, 'suite', 'A larger private or semi-private living space, often including a living area or kitchenette.', 'https://images.pexels.com/photos/6510951/pexels-photo-6510951.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', '2024-11-26 06:52:16', '2024-11-26 06:52:16');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `role_id` bigint(20) NOT NULL DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role_id`, `created_at`, `updated_at`) VALUES
(16, 'diego.romero1798@alumnos.udg.mx', 'scrypt:32768:8:1$CkWhm4zgpTIgdmHc$41063f7cdc3dff536ed3b75bdb6239237fdb7519b0236cb915bd1c8c669fca4d54e7dfc31946b61210b3b6799799aed2813af3b42f5a5d69ed1c2e6e3497a9b3', 2, '2024-11-27 01:25:24', '2024-11-27 01:25:24'),
(17, 'admin@admin.com', 'admin', 2, '2024-11-27 04:57:34', '2024-11-27 04:57:34');

-- --------------------------------------------------------

--
-- Table structure for table `visits`
--

CREATE TABLE `visits` (
  `id` bigint(20) NOT NULL,
  `guest_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `visit_date` date NOT NULL,
  `purpose` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `guests`
--
ALTER TABLE `guests`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `occupants`
--
ALTER TABLE `occupants`
  ADD PRIMARY KEY (`id`),
  ADD KEY `guest_id` (`guest_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `room_id` (`room_id`);

--
-- Indexes for table `order_history`
--
ALTER TABLE `order_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `visit_id` (`visit_id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `occupant_id` (`occupant_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`) USING HASH;

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `room_number` (`room_number`) USING HASH,
  ADD UNIQUE KEY `rooms name` (`name`) USING HASH,
  ADD KEY `room_type_id` (`room_type_id`),
  ADD KEY `room_type_photo` (`room_type_photo`(768)) USING BTREE;

--
-- Indexes for table `room_orders`
--
ALTER TABLE `room_orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `room_id` (`room_id`);

--
-- Indexes for table `room_types`
--
ALTER TABLE `room_types`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `type_name` (`type_name`) USING HASH,
  ADD KEY `photo` (`photo`(768)) USING BTREE;

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`) USING HASH,
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `visits`
--
ALTER TABLE `visits`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `guest_id` (`guest_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `guests`
--
ALTER TABLE `guests`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `occupants`
--
ALTER TABLE `occupants`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `order_history`
--
ALTER TABLE `order_history`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `rooms`
--
ALTER TABLE `rooms`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `room_orders`
--
ALTER TABLE `room_orders`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `room_types`
--
ALTER TABLE `room_types`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `visits`
--
ALTER TABLE `visits`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `occupants`
--
ALTER TABLE `occupants`
  ADD CONSTRAINT `occupants_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `occupants_ibfk_2` FOREIGN KEY (`guest_id`) REFERENCES `guests` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `occupants_ibfk_3` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `order_history`
--
ALTER TABLE `order_history`
  ADD CONSTRAINT `order_history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `order_history_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `room_orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `order_history_ibfk_3` FOREIGN KEY (`visit_id`) REFERENCES `visits` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `order_history_ibfk_4` FOREIGN KEY (`occupant_id`) REFERENCES `occupants` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `rooms`
--
ALTER TABLE `rooms`
  ADD CONSTRAINT `rooms_ibfk_1` FOREIGN KEY (`room_type_id`) REFERENCES `room_types` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `room_orders`
--
ALTER TABLE `room_orders`
  ADD CONSTRAINT `room_orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `room_orders_ibfk_2` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `visits`
--
ALTER TABLE `visits`
  ADD CONSTRAINT `visits_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `visits_ibfk_2` FOREIGN KEY (`guest_id`) REFERENCES `guests` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
