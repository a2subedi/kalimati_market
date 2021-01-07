# create a table for commodity if it doesnot exist.
create_stmt = '''CREATE TABLE IF NOT EXISTS `{}` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `max` DOUBLE(7,2) NULL,
  `min` DOUBLE(7,2) NULL,
  `avg` DOUBLE(7,2) NULL,
  `date` DATE NULL,
  PRIMARY KEY (`id`));'''


# Insert a commodity row into commodity table. (global commodity table)
insert_commodity = '''INSERT INTO `commodity` (`name`, `unit`, `max`, `min`, `avg`, `date`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}');'''


#Insert a commodity into its own table for the date.
insert_item_date = '''INSERT INTO `{}` (`max`, `min`, `avg`, `date`) VALUES ('{}', '{}', '{}', '{}');'''