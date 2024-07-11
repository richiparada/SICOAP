import { Component, OnInit } from '@angular/core';
import { ProveedoresService, Proveedor } from '../proveedores.service';

@Component({
  selector: 'app-proveedores',
  standalone: true,
  imports: [],
  templateUrl: './proveedores.component.html',
  styleUrl: './proveedores.component.css'
})
export class ProveedoresComponent implements OnInit {
  proveedores: Proveedor[] = [];

  constructor(private proveedoresService: ProveedoresService) { }

  ngOnInit(): void {
    this.proveedoresService.getProveedores().subscribe(data => {
      this.proveedores = data;
    });
  }

  addProveedor(nombre: string, empresa: string, numero_contacto: string): void {
    const newProveedor: Proveedor = { id: 0, nombre, empresa, numero_contacto };
    this.proveedoresService.addProveedor(newProveedor).subscribe(proveedor => {
      this.proveedores.push(proveedor);
    });
  }

  deleteProveedor(proveedor: Proveedor): void {
    this.proveedoresService.deleteProveedor(proveedor.id).subscribe(() => {
      this.proveedores = this.proveedores.filter(p => p !== proveedor);
    });
  }
}