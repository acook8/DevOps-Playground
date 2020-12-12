import React from 'react';
import { Button, Form, Modal, ModalFooter } from "react-bootstrap";


function UsersModal() {
    const [show, setshow] = React.useState(false);
    const handleClose = () => setshow(false);
    const handleShow = () => show(true);

    const [firstName, setFirstName] = React.useState("");
    const [lastName, setLastName] = React.useState("");
    const [age, setAge] = React.useState("");
    const [address, setAddress] = React.useState("");


    const handleSubmit = (event) => {
        console.log(`
          First Name: ${firstName}
          Last Name: ${lastName}
          Age: ${age}
          Address: ${address}
        `);

        event.preventDefault();
    }

    return (
        <>
            <Button onClick={handleShow}>Add User</Button>
            <Modal.Dialog>
                <Modal.Header closeButton>
                    <Modal.Title>Add User</Modal.Title>
                </Modal.Header>
                
                <Modal.Body>
                    <Form onSubmit={handleSubmit}>
                    <Form.Group controlId="formFirstName" onChange={e => setFirstName(e.target.value)}>
                        <Form.Label>First Name</Form.Label>
                        <Form.Control value={firstName} required></Form.Control>
                    </Form.Group>

                    <Form.Group controlId="formLastName" onChange={e => setLastName(e.target.value)}>
                        <Form.Label>Last Name</Form.Label>
                        <Form.Control value={lastName} required></Form.Control>
                    </Form.Group>

                    <Form.Group controlId="formAge" onChange={e => setAge(e.target.value)}>
                        <Form.Label>Age</Form.Label>
                        <Form.Control value={age} required></Form.Control>
                    </Form.Group>

                    <Form.Group controlId="formAddress" onChange={e => setAddress(e.target.value)}>
                        <Form.Label>Address</Form.Label>
                        <Form.Control value={address} required ></Form.Control>
                    </Form.Group>

                </Form>
                </Modal.Body>

                <ModalFooter>
                    <Button variant="secondary" onClick={handleClose}>Close</Button>
                    <Button variant="primary" onClick={handleSubmit}>Save</Button>
                </ModalFooter>

                
            </Modal.Dialog>


        </>

    );
}
export default UsersModal;