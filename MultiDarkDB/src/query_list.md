Query 1
=======

select top 10 * from miniMDR1..FOF where snapnum = 85 order by np desc

Query 2
=======

select fofId, x, y, z, vx, vy, vz, mass from miniMDR1..FOF f 
where f.snapnum=85
  and f.x between 390 and 392

Query 3
=======

with my_halo as (
   select x,y,z from miniMDR1..FOF where snapnum=85 and fofId=85000004639
)

select f.* from my_halo mh, miniMDR1..FOF f 

where f.snapnum = 85
 and  f.x between (mh.x - 3) and (mh.x + 3)
 and  f.y between (mh.y - 3) and (mh.y + 3)
 and  f.z between (mh.z - 3) and (mh.z + 3)


Query 4
=======

with MyHalo as (
     select * from MDR1..FOF
        where snapnum=85
	and fofId=85000004639
),

fofHaloParticles as (
    select fP.* from MDR1..FOFParticles fP,
            MyHalo mH
        where fP.fofId = mH.fofId
            and fP.snapnum=85
)

select p.* from fofHaloParticles hP, MDR1..particles p
    where p.particleId = hP.particleId
