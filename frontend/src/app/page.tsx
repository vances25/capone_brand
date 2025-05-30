"use client";

import styles from "./page.module.css";
import { useState, useEffect } from "react";
import { useRouter } from 'next/navigation';



interface Links{
  "instagram": string,
  "telegram": string
}

export default function Home() {

  const [currentLinks, setCurrentLinks] = useState<Links | undefined>()


  const [showForum, setShowForum] = useState<boolean>(false)

  const [username, setUsername] = useState<string>("")
  const [phone, setPhone] = useState<string>("")
  const [submitError, setSubmitError] = useState<string | undefined>()

  const router = useRouter()


  const url = process.env.NEXT_PUBLIC_API_URL

  console.log(url)

  const SubmitNumber = () =>{
    if(username !== "" && phone !== ""){
      fetch(`${url}/request_number`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          phone: phone,
          username: username,
        })
      })
      .then((res) => res.json())
      .then((data) => {
        setSubmitError("Success!")
        setUsername("")
        setPhone("")
    })
      .catch((e)=>{
        console.log(e)
        setSubmitError("please wait one moment and try again")
      })
    }else{
      setSubmitError("please provide some information")
    }
  }


  useEffect(()=>{
    fetch(`${url}/socials`)
    .then(res=>res.json())
    .then(data =>{
      setCurrentLinks(data)
    }
    )
    .catch(e=>console.log(e))
  }, [])

  return (
    <>

    
    <div className={styles.container}>


      <div className={styles.logo}>
      <img id="logo" src="/logo.png"></img>
      </div>
      
      <section className={styles.banner}>
      <div className={styles.showcase}>
        <h3>Tested. Trusted. Transparent.</h3>
        <img src="/pot.png" alt="test"></img>
      </div>
      </section>


      <div className={styles.join}>
        <button onClick={()=> router.push(currentLinks ? currentLinks.telegram : "/")}>Join Telegram <img src="/telegram.png"/></button>
        <button onClick={()=> setShowForum(!showForum)}>Request Phone # <img src="/phone.png"/></button>
      </div>

      {showForum &&
      <div className={styles.forum}>
         <hr></hr>

        <h1>Submit Phone #</h1>


        <div>
        <label htmlFor="name">Name/Nickname:</label>
        <input value={username} onChange={(e)=> setUsername(e.target.value)} id="name"></input>
        <br/>

          <div>
        <label htmlFor="phone">Phone #:</label>
        <input value={phone} onChange={(e)=> setPhone(e.target.value)} id="phone"></input>
          </div>
        </div>


        <button onClick={()=>SubmitNumber()}>Submit</button>
        <p>{submitError}</p>
      </div>
      }


      <div className={styles.section_divider}>

      </div>

      <section className={styles.main_mission}>
        <div className={styles.mission}>
          <h1>Our Mission</h1>
          <p>
          At Cee Cee Packs, real means everything.<br/><br/>
          No cut corners. No mystery oils. No watered-down flower.<br/><br/>
          Just honest, lab-tested cannabis — loud, clean, and exactly what we say it is.<br/><br/>
          For those who care about what they smoke and who they get it from.
          </p>
        </div>
      </section>


      <div className={styles.section_divider2}>

      </div>


      <section className={styles.footer}>
        <div className={styles.in_footer}>
          <p>Ready to tap in with the real ones?</p>

        <div className={styles.socials}>
          <a href={currentLinks ? currentLinks.telegram: "/"}><img src="/telegram.png" alt="Telegram" /></a>
          <a href={currentLinks ? currentLinks.instagram: "/"}><img src="/instagram.webp" alt="Instagram" /></a>
        </div>


          <a>ACTIVE RN {new Date().getFullYear()}</a>
        </div>
      </section>

    </div>
    </>
  );
}
