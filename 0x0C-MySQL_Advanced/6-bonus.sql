-- SQL script that creates a stored procedure AddBonus that adds a new
-- correction for a student
DELIMITER //
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
	SET @proj_id := (SELECT id FROM projects where name = project_name);
	IF (@proj_id is NULL) THEN
	   INSERT INTO projects (name) VALUES (project_name);
	   SET @proj_id := LAST_INSERT_ID();
	END IF;
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @proj_id, score);
END //
DELIMITER ;
