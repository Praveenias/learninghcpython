<div>
    <div class="container card bg-light p-3" >
        @if(session('success'))
        <p class="alert alert-success">{{session('success')}}</p>
        @endif
        <form class="row g-3" wire:submit="save">
            <h3 class="text-center">User Registartion</h3>
            <div class="col-md-6">
                <label for="inputEmail4" class="form-label">Email</label>
                <input type="email" class="form-control" id="inputEmail4" wire:model.live="form.email">{{$form->email}}
                @error('form.email')
                <span class="text-danger">{{ $message }}</span>
                @enderror
            </div>
            <div class="col-md-6">
                <label for="inputPassword4" class="form-label">Password</label>
                <input type="password" class="form-control" id="inputPassword4" wire:model="form.password">
                @error('form.password')
                <span class="text-danger">{{ $message }}</span>
                @enderror
            </div>

            <div class="col-md-3">
                <label for="inputZip" class="form-label">Name</label>
                <input type="text" class="form-control" id="inputZip" wire:model="form.name">
                @error('form.name')
                <span class="text-danger">{{ $message }}</span>
                @enderror
            </div>

            <div class="col-12">
            <button class="btn btn-primary" type="submit">
                <span wire:loading class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                <span class="sr-only">Save</span>
            </button>
                <!-- <button type="submit" class="btn btn-primary">Save</button> -->
                <a class="btn btn-primary"  href="/" wire:navigate>Back</a>
            </div>
            
        </form>
    </div>
    
</div>