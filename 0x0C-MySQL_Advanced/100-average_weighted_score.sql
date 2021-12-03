-- script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and stores the average weighted score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
	SET @wtd_score := (SELECT SUM(score * weight) / SUM(weight)
	    FROM corrections LEFT JOIN projects
	    ON corrections.project_id = projects.id
	    WHERE user_id = corrections.user_id);
	UPDATE users SET average_score = @wtd_score WHERE id = user_id;
END //
DELIMITER ;
