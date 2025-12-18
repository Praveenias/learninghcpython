<?php

namespace App\Livewire\Users;

use App\Livewire\Forms\UserForm;
use App\Models\User;
use Livewire\Component;
use Livewire\Attributes\Rule;
use Livewire\Attributes\Locked;

class EditUsers extends Component
{  
    public UserForm $form;

    public function mount(User $user){
    // {   $this->userId = $user->id;
    //     $this->name = $user->name;
    //     $this->email = $user->email;
    //     $this->password = $user->password; 
        $this->form->setUser($user);
       
    }

    public function save(){
        $this->form->update();
        // $this->validate();
        // User::where('id', $this->userId)->update($this->only(['name', 'email', 'password'])); 
 
        $this->redirect('/');
    }
    public function render()
    {
        return view('livewire.users.edit-users');
    }
}
