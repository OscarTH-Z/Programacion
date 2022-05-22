from Process_data import Process_Data

def main():
	process_data = Process_Data()


	print("1. Conectarse al enlace")
	url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
	data = process_data.get_data_from_link(url)

	print("2. Obtener el número de respuestas contestadas y no contestadas")
	print(process_data.get_answers(data))

	print("3. Obtener la respuesta con menor número de vistas")
	print(process_data.get_answer_with_least_number_of_views(data))

	print("4. Obtener la respuesta más vieja y más actual")
	print(process_data.get_the_oldest_and_most_recent_response(data))


	print("5. Obtener la respuesta del owner que tenga una mayor reputación")
	print(process_data.get_owner_with_the_highest_reputation(data))



if __name__== "__main__" :
	main()







"""

/*SELECT NOMBRE_AEROPUERTO FROM AEROPUERTOS WHERE ID_AEROPUERTO IN (
	SELECT ID_AEROPUERTO
	FROM VUELO
	GROUP BY ID_AEROPUERTO
	HAVING COUNT(*) = 
	(
		SELECT MAX(total_movimientos) FROM (
			SELECT 
				ID_AEROPUERTO,
				COUNT(*) AS total_movimientos
			FROM VUELO
			GROUP BY 1
			ORDER BY 2 DESC
			LIMIT 1
		) AS conteo
	)	
)*/

/*SELECT NOMBRE_AEROLINEA FROM AEROLINEA WHERE ID_AEROLINEA IN (
	SELECT ID_AEROLINEA
	FROM VUELO
	GROUP BY ID_AEROLINEA
	HAVING COUNT(*) = 
	(
		SELECT MAX(total_movimientos) FROM (
			SELECT 
				ID_AEROLINEA,
				COUNT(*) AS total_movimientos
			FROM VUELO
			GROUP BY 1
			ORDER BY 2 DESC
			LIMIT 1
		) AS conteo
	)	
)

SELECT DIA
	FROM VUELO
	GROUP BY DIA
	HAVING COUNT(*) = 
	(
		SELECT MAX(total_movimientos) FROM (
			SELECT 
				DIA,
				COUNT(*) AS total_movimientos
			FROM VUELO
			GROUP BY 1
			ORDER BY 2 DESC
			LIMIT 1
		) AS conteo
	)"""