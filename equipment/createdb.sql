BEGIN;
CREATE TABLE `equipment_equipment` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL UNIQUE
) DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
CREATE TABLE `equipment_application` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(300) NOT NULL,
    `organization` varchar(300) NOT NULL,
    `email` varchar(75) NOT NULL,
    `phone` varchar(20) NOT NULL,
    `content` longtext NOT NULL,
    `status` varchar(1) NOT NULL,
    `equipment_id` integer,
    `startdate` date NOT NULL,
    `enddate` date NOT NULL,
    `created` datetime NOT NULL,
    `updated` datetime NOT NULL,
    `unum` varchar(32) NOT NULL
) DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
ALTER TABLE `equipment_application` ADD CONSTRAINT `equipment_id_refs_id_0ec3d022` FOREIGN KEY (`equipment_id`) REFERENCES `equipment_equipment` (`id`);
CREATE INDEX `equipment_application_3ec02a90` ON `equipment_application` (`equipment_id`);
COMMIT;
