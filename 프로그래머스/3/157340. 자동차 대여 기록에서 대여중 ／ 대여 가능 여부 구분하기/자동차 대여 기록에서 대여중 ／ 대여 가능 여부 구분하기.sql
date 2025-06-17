SELECT CAR_ID,
    CASE 
        WHEN EXISTS (# CAR_Id 중에 하나가 조건에 만족 한다면
            SELECT 1
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as c2
            WHERE '2022-10-16' between START_DATE and END_DATE and c1.CAR_ID = c2.CAR_ID # 이조건이 있으면 외부 쿼리에서 CAR_ID가 1001일때 내부 쿼리도 그 값에 대한 것만 조건을 검사하기 때문에 나누어서  검사함 
        )
        THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as c1
GROUP BY CAR_ID
ORDER BY CAR_ID DESC