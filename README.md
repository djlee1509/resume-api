# Resume (CV) as an API

## Idea
- Lots of managers asked for the experience of creating an API so, I have decided to create an API for my resume/ CV.

- Prospective employers/ engineering manager will be able to send GET request to gain details of my CV.

- The REST API will be created using Python and Flask.

## Usage

**Method**
----
 `GET`

**End Points**
----
  * `/resume`: returns json data of a whole Resume/ CV
  
  * `/profile`: returns profile, brief introduction in a list.
  
  * `/contact/{contact_detail}`: returns contact details
   contact_detail: email, github, phone, none - returns json data (contact details) `email`, `github` and `phone`.
   
  * `/skills/{skill}`: returns json data of skills. 
   skill: `technical_skills`, `languages`, none - returns both skills (technical skills, languages)
   
  * `/{section}/:number`
  section: experience, projects, education
  number: 1 - 6 (1: most recent, 6: oldest) <br/>
  e.g. `/experience/1` - returns most recent work experience
  
  * `/interests`: returns a list of interests
  
**URL**
----
 `https://dlee-cv-api.herokuapp.com/`

**Sample Call:**
----
  ```bash
    curl https://dlee-cv-api.herokuapp.com/{endpoint}
  ```

## What I have learned
* Creating a REST API using Python, Flask.
