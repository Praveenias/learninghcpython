import Contactcard from "./contactcard"


const ContactList = (props) => {

    const renderlist = props.contacts.map((contact)=>{
       return <Contactcard data1={contact}/>
    })
    return(
        <div className="ui celled list">
            {renderlist}
        </div>
    )
}

export default ContactList;