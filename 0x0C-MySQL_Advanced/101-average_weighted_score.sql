-- script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and stores the average weighted score for all students
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users
	    SET average_score = (SELECT SUM(score * weight) / SUM(weight)
	    FROM corrections INNER JOIN projects
	    ON corrections.project_id = projects.id
	    WHERE users.id = corrections.user_id);
END //
DELIMITER ;
