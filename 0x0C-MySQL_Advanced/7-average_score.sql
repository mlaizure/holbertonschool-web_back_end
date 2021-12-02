-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- computes and stores the average score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	SET @avg_score := (SELECT AVG(score) FROM corrections where corrections.user_id = user_id);
	UPDATE users SET average_score = @avg_score WHERE id = user_id;
END //
DELIMITER ;
