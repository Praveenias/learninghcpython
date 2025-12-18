<?php

namespace App\Livewire\Forms;

use App\Models\User;
use Livewire\Attributes\Rule;
use Livewire\Form;

class UserForm extends Form
{

    public ?User $user;
    #[Rule('required|min:5')]
    public string $name = '';

    #[Rule('required|email')]
    public string $email = '';
    
    #[Rule('required')]
    public string $password ;

    public function setUser($user){
        $this->user = $user;
        $this->name = $user->name;
        $this->email = $user->email;
        $this->password = $user->password; 
    }
 
    public function save(): void
    {
        $this->validate();
 
        User::create($this->all());
    }

    public function update(): void 
    {
        $this->validate();
 
        $this->user->update($this->all());
    }
}
