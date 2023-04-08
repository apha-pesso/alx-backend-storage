-- Procedure for average score
-- store average score for a student
DELIMITER $;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    	DECLARE avearge_score FLOAT;
    	SELECT AVG(score) INTO avearge_score FROM corrections
    	WHERE user_id = corrections.user_id;
   	UPDATE users
	SET average_score = avearge_score
	WHERE id = user_id;
END;
$
