<?php

namespace App\Livewire\Users;

use App\Livewire\Forms\UserForm;
use Livewire\Component;

class CreateUsers extends Component
{
    public UserForm $form; 

    public function save(): void
    {
        $this->form->save();  
        $this->redirect('/');
    }
    public function render()
    {
        return view('livewire.users.edit-users');
    }
}
